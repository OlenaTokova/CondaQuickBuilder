# Filename: main5.py
# Docstring needed...

# TODO: add try-except blocks to make all parts of the program  fault-tolerant. 
# 
# Derived from main4.py where Copilot added logging.  
# This is the first version of the CondaQuickBuiler with Logging.
import os
import re
import logging
import zipfile
import requests
import datetime
import subprocess
from packaging.version import parse, InvalidVersion

# Set up logging
log_filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_CondaQuickBuilder_DebugLog.log"
logging.basicConfig(filename=log_filename, level=logging.DEBUG)
print(f"\nLog file '{log_filename}' has been created in: {os.getcwd()}\n")  # FOR DEBUGGING

# TODO: convert this try-except block to a function and add a docstring to it
try:
    # Get the latest version of Python available
    result = requests.get("https://endoflife.date/api/python.json")
    parsed_result = result.json()
    logging.info(f"parsed_result {parsed_result}")

    last_python_version =  str(parsed_result[0]["latest"])
    logging.info(f"latest_python_version {last_python_version}")
except Exception as e:
    logging.error(f"Error occurred while getting the latest Python version: {e}")

# Define the minimum and maximum acceptable Python versions
MIN_PYTHON_VERSION = parse("2.0")
MAX_PYTHON_VERSION = parse(last_python_version)

def unzip_starter_project_repo():
    """
    Unzip a starter project repository.

    Returns:
    None
    """
    try:
        # Get the name of the zip file from the user
        zip_file_name = input("Enter the name of the zip file: ")

        # Create a ZipFile object
        with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
            # Extract all the contents of the zip file in the current directory
            zip_ref.extractall()
        
        zip_file_name = zip_file_name[:-4]
        logging.info(f"Unzipped project repository: {zip_file_name}")
        return zip_file_name
    except Exception as e:
        logging.error(f"Error occurred while unzipping the project repository: {e}")

requirements = []
def parse_requirements(pathtorequirements):
    """
    Parse requirements from a requirements file and return a list of tuples containing module, version sign, and version.
    
    :param pathtorequirements: The path to the requirements file
    :type pathtorequirements: str
    :return: A list of tuples containing module, version sign, and version
    :rtype: list
    """
    global requirements
    try:
        with open(f'{pathtorequirements}/requirements.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):  # ignore empty lines and comments
                    match = re.match(r'([a-zA-Z0-9_.-]+\[?[a-zA-Z0-9_.-]*\]?)([<=>]+)?([\d.a-zA-Z-]*)?', line)
                    if match:
                        module, version_sign, version = match.groups()
                        requirements.append((module, version_sign, version))
                    else:
                        # handle packages without version specification
                        requirements.append((line, None, None))
    except Exception as e:
        logging.error(f"Error occurred while parsing the requirements.txt file: {e}")

def get_envs():
    """
    Function to retrieve a list of available pre-existing conda environments.
    Returns a list of environment names.
    """
    try:
        result = subprocess.run(['conda', 'env', 'list'], stdout=subprocess.PIPE)
        envs = result.stdout.decode('utf-8').splitlines()
        env_names = [line.split()[0] for line in envs if not line.startswith('#') and line.split()]
        return env_names
    except Exception as e:
        logging.error(f"Error occurred while using get_envs() while to retrieve a list of all existing conda environments: {e}")

def get_channels():
    """
    Retrieves a list of channels from the conda configuration. 
    Returns a list of channel names.
    """
    try:
        result = subprocess.run(['conda', 'config', '--show', 'channels'], stdout=subprocess.PIPE)
        # Decode the output to a string and split into lines
        channels_output = result.stdout.decode('utf-8').splitlines()
        # Initialize an empty list to hold channel names
        channels_names = []
        # Iterate through each line in the output
        for line in channels_output:
            # Check if the line starts with "  - " which indicates a channel name
            if line.strip().startswith('-'):
                # Split the line by spaces and take the last element as the channel name
                channel_name = line.split()[-1]
                # Append the channel name to the list
                channels_names.append(channel_name)
        return channels_names
    except Exception as e:
        logging.error(f"Error occurred while retrieving conda channels using get_channels(): {e}")

def get_package_versions(env, package):
    """
    Retrieves the version of a specified package in a given environment using conda.
    # TODO: should this function be called get_package_version() or get_package_version_in_env()?
    Args:
        env (str): The name of the conda environment.
        package (str): The name of the package.

    Returns:
        str: A string containing the version of the specified package in the given environment.
    """
    try:
        result = subprocess.run(['conda', 'list', '-n', env, package], stdout=subprocess.PIPE)
        print(f"The Result of subprocess assigned to 'result' is: {result}")   # FOR DEBUGGING
        logging.info(f"Result of subprocess: {result}")
        
        versions = result.stdout.decode('utf-8')
        print(f"The result assigned to 'versions' is: {versions}")  # FOR DEBUGGING 
        logging.info(f"Decoded versions: {versions}")
        
        return versions
    except Exception as e:
        logging.error(f"Error occurred while retrieving package version using get_package_versions() function: {e}")

def save_versions(package):
    """
    Save the package version if it exists in an environment to a file. 
    
    TODO: clarify the exact purpose(s) of this function.
    Save versions of a package for all environments to a file.
    TODO: Change "conda_versions_all_envs.txt" to a variable or parameter.
    Args:
        package: The package for which versions are to be saved.
    
    Returns:
        None
    """
    try:
        envs = get_envs()
        with open('conda_versions_all_envs.txt', 'w') as f:
            for env in envs:
                f.write(f'Environment: {env}\n')
                f.write(get_package_versions(env, package))
                f.write('\n')
    except Exception as e:
        logging.error(f"Error occurred while saving versions using save_versions(package): {e}")

def create_conda_env(env_name, python_version):
    """
    Create a new conda environment.

    Parameters:
    env_name (str): The name of the conda environment.

    Returns:
    None
    """
    try:
        # Create a new conda environment
        subprocess.run(["conda", "create", "--name", env_name, "python={python_version}" ,"--yes"], check=True)
        subprocess.run(["conda", "install", "-n", env_name, "pip","--yes"], check=True)
    except Exception as e:
        logging.error(f"Error occurred while creating conda environment using create_conda_env(env_name, python_version): {e}")

def search_pypi(package, package_sign, package_version):
    """
    Searches PyPI for a package and filters the releases based on the given version sign and version number.
    Returns the highest version that matches the criteria. Supports wildcard '*' in package_version for matching any minor/patch version.

    Args:
        package (str): The name of the package to search for.
        package_sign (str): The comparison operator ("==", "<=", or "~=").
        package_version (str): The version number to compare against, supports wildcard '*' for minor/patch versions.

    Returns:
        str: The highest version number that matches the given criteria or None if no matches found.
    """
    try:
        url = f"https://pypi.org/pypi/{package}/json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            releases = data.get("releases", {})
            valid_versions = []

            for release in releases:
                try:
                    release_ver = parse(release)
                    if '*' in package_version:
                        base_version = package_version.rstrip('*')
                        if str(release).startswith(base_version):
                            valid_versions.append(release_ver)
                    else:
                        if package_sign == "==":
                            if release_ver == parse(package_version):
                                valid_versions.append(release_ver)
                        elif package_sign == "<=":
                            if release_ver <= parse(package_version):
                                valid_versions.append(release_ver)
                        elif package_sign == "~=":
                            if release_ver.major == parse(package_version).major and release_ver >= parse(package_version):
                                valid_versions.append(release_ver)
                except InvalidVersion:
                    continue

            if valid_versions:
                # Find the highest version from the valid_versions list
                highest_version = max(valid_versions)
                return str(highest_version)
        return None
    except Exception as e:
        logging.error(f"Error occurred while searching PyPI: {e}")
        

# TODO: split the steps in search_package into separate functions?  
# TODO: add try-except blocks to make this fault-tolerant. 

def search_package(package, package_sign, package_version, channels_list):
    """
    Search for a package in Conda Forge, Anaconda, and PIP repositories.

    Parameters:
    package (str): The name of the package.

    Returns:
    str: The repository where the package was found, or None if it wasn't found.
    """
    
    global conda_packages, pip_packages
    
    # Loop through the channels
    for channel in channels_list:
        if channel == "defaults":
            channel = "anaconda"
        result = subprocess.run(["conda", "search", "-c", channel, f"{package}{package_sign}{package_version}"], stdout=subprocess.PIPE)
        if package in result.stdout.decode():
            # Install conda package in the environment
            conda_install_cmd = ["conda", "install", "--yes", "--name", env_name, "-c", channel, f"{package}{package_sign}{package_version}"]
            print(f'Try to install {conda_install_cmd}')
            subprocess.run(conda_install_cmd, check=True)
            print (f"Package '{package} {package_version}' found in '{channel}' channel. And installed in environment '{env_name}'")
            return channel
        
    # Search in PIP

    version = search_pypi(package, package_sign, package_version)
    if version:
   
        pip_packages_versions = f"{package}={version} "
        # Install pip packages
        # using this version "conda run -n ETC_tools python -m pip install pandas==1.3.5"
        print(f'Try to install {pip_packages_versions}')
        subprocess.run(["conda", "run", "-n", env_name, "python", "-m", "pip", "install", pip_packages_versions], check=True)
        print (f"Package '{package} {package_version}' found in 'PyPI' channel. And installed in environment '{env_name}'")
        return version
    
    print(f"Package '{package} {package_version}' not found in any channel.")
    return None

# TODO: make main() into a separate function that is the main "entry point" for the program.  

# TODO: get logic clearer and more organized for main:
# 1. Unzip the starter project repository
# 2. Ask the user for the Python version
# 3. Parse the requirements file
# 4. Get the list of channels
# 5. Get the list of environments
# 6. Create a new environment
# 7. Install the packages in the environment
# 8. Save the versions of the packages (?) to a file

    
# TODO: After each step, add a log message to indicate that the step has been completed successfully.
    
if __name__ == "__main__":
    # unzip and get project folder name
    project_folder_name = unzip_starter_project_repo()

    
    try: 
        while True:
            # TODO: ask the user if they want to use the latest Pythnon version or if not, which earlier version they want to use.
            python_version = input("Enter Python version for environment (e.g., 3.7.4): ")
            
            # Check if the entered version matches the pattern for Python versions
            # TODO: add a function to check if the version is within the acceptable range
            if re.match(r'^\d+\.\d+(\.\d+)?$', python_version):
                parsed_version = parse(python_version)
                # Check if the version is within the acceptable range
                if MIN_PYTHON_VERSION <= parsed_version <= MAX_PYTHON_VERSION:
                    print(f"You have entered Valid Python version: {python_version}\n")
                    break  # Version is valid; exit the loop
                else:
                    print(f"Python version {python_version} is out of the acceptable range ({MIN_PYTHON_VERSION} - {MAX_PYTHON_VERSION}).")
            else:
                print("Invalid format. Please enter a valid Python version (e.g., '3.7.4').")

            # parse requirements
            parse_requirements(project_folder_name)
            
            # get channels_list returned from get_channels()
            channels_list = get_channels()

            envs_list = get_envs()
            env_name = ""
            while True:
                env_name = input("Enter your NEW Environment Name: ")
                if env_name not in envs_list:
                    create_conda_env(str(env_name), python_version)
                    print(f"Environment '{env_name}' has been created.")
                    break  # Exit the loop
                else:
                    print(f"Environment '{env_name}' already exists. Please enter a different environment name.")

            if requirements:
                for requirement in requirements:
                    package = requirement[0]
                    package_sign = requirement[1]
                    package_version = requirement[2]
                    search_package(package, package_sign, package_version, channels_list)
    except Exception as e:
        logging.error(f"Error occurred in main: {e}")

    # Save versions of a package for all environments to a file
    
save_versions(package)  

logging.info(f"Versions of package {package} saved to conda_versions_all_envs.txt in {os.getcwd()}")

print(f"Versions of package {package} saved to conda_versions_all_envs.txt")

    # print(f"Environment {env_name} created successfully with Python version {python_version}")
    # logging.info(f"Environment {env_name} created successfully with Python version {python_version}")

    # print(f"Package {package} installed successfully in environment {env_name}")
    # logging.info(f"Package {package} installed successfully in environment {env_name}")

    # print(f"Versions of package {package} saved to conda_versions_all_envs.txt")
