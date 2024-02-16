"""Docstring for main3.py"""

import re
import subprocess
import requests
import zipfile
from packaging.version import parse, InvalidVersion

def unzip_starter_project_repo():
    """
    Unzip a starter project repository.

    Returns:
    None
    """
    # Get the name of the zip file from the user
    zip_file_name = input("Enter the name of the zip file: ")

    # Create a ZipFile object
    with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
        # Extract all the contents of the zip file in the current directory
        zip_ref.extractall()
    
    zip_file_name = zip_file_name[:-4]
    
    return zip_file_name

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

def get_envs():
    """
    Function to retrieve a list of available conda environments.
    Returns a list of environment names.
    """
    result = subprocess.run(['conda', 'env', 'list'], stdout=subprocess.PIPE)
    envs = result.stdout.decode('utf-8').splitlines()
    env_names = [line.split()[0] for line in envs if not line.startswith('#') and line.split()]
    return env_names

def get_channels():
    """
    Retrieves a list of channels from the conda configuration. 
    Returns a list of channel names.
    """
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

def get_package_versions(env, package):
    """
    Retrieves the versions of a specified package in a given environment using conda.

    Args:
        env (str): The name of the conda environment.
        package (str): The name of the package.

    Returns:
        str: A string containing the versions of the specified package in the given environment.
    """
    result = subprocess.run(['conda', 'list', '-n', env, package], stdout=subprocess.PIPE)
    versions = result.stdout.decode('utf-8')
    return versions

def save_versions(package):
    """
    Save versions of a package for all environments to a file.
    
    Args:
        package: The package for which versions are to be saved.
    
    Returns:
        None
    """
    envs = get_envs()
    with open('conda_versions_all_envs.txt', 'w') as f:
        for env in envs:
            f.write(f'Environment: {env}\n')
            f.write(get_package_versions(env, package))
            f.write('\n')

def create_conda_env(env_name):
    """
    Create a new conda environment.

    Parameters:
    env_name (str): The name of the conda environment.

    Returns:
    None
    """
    # Create a new conda environment
    subprocess.run(["conda", "create", "--name", env_name, "--yes"], check=True)

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
            channels_packages_versions = f"-c {channel} {package}{package_sign}{package_version} "
            subprocess.run(["conda", "install", "--yes", "--name", env_name, channels_packages_versions], check=True)
            print (f"Package '{package} {package_version}' found in '{channel}' channel. And installed in environment '{env_name}'")
            return channel
        
    # Search in PIP
    version = search_pypi(package, package_sign, package_version)
    if version:
   
        pip_packages_versions = f"{package}={version} "
        # Install pip packages
        # using this version "conda run -n ETC_tools python -m pip install pandas==1.3.5"
        subprocess.run(["conda", "run", "-n", env_name, "python", "-m", "pip", "install", pip_packages_versions], check=True)
        print (f"Package '{package} {package_version}' found in 'PyPI' channel. And installed in environment '{env_name}'")
        return version

    print(f"Package '{package} {package_version}' not found in any channel.")
    return None

if __name__ == "__main__":
    # unzip and get project folder name
    project_folder_name = unzip_starter_project_repo()
     
    # parse requirements
    parse_requirements(project_folder_name)
    
    #get channels list
    channels_list = get_channels()

    env_list = get_envs()
    env_name = ""
    while True:
        env_name = input("Enter Environment Name: ")
        if env_name not in env_list:
            create_conda_env(str(env_name))
            print(f"Environment '{env_name}' has been created.")
            break  # Exit the loop
        else:
            print(f"Environment '{env_name}' already exists. Please enter a different environment name.")

    if requirements:
        for requirment in requirements:
            package = requirment[0]
            package_sign = requirment[1]
            package_version = requirment[2]
            search_package(package, package_sign, package_version, channels_list)
    