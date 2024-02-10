import re
import subprocess
import requests
import zipfile

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

def parse_requirements(pathtorequirements):
    requirements = []
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
    return requirements

def get_envs():
    result = subprocess.run(['conda', 'env', 'list'], stdout=subprocess.PIPE)
    envs = result.stdout.decode('utf-8').splitlines()
    env_names = [line.split()[0] for line in envs if not line.startswith('#') and line.split()]
    return env_names

def get_channels():
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
    result = subprocess.run(['conda', 'list', '-n', env, package], stdout=subprocess.PIPE)
    versions = result.stdout.decode('utf-8')
    return versions

def save_versions(package):
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
    Search for a package on PyPI.

    Parameters:
    
    package (str): The name of the package.

    Returns:
    bool: True if the package was found, False otherwise.
    """
    
    response = requests.get(f"https://pypi.org/pypi/requests/json")
    print(response)
    if "releases" in response:
        # Return the list of keys in the "releases" dictionary, which are the version numbers
        return list(response["releases"].keys())
    else:
        # If "releases" key is not found, return an empty list
        return []



    """
    data = response.json()
    if data.get("message"):
        if data["message"] != "Not Found":
            return True
    else:
        return True
    return False
    """

def search_package(package, package_sign, package_version, channels_list):
    """
    Search for a package in Conda Forge, Anaconda, and PIP repositories.

    Parameters:
    package (str): The name of the package.

    Returns:
    str: The repository where the package was found, or None if it wasn't found.
    """
    # Loop through the channels
    for channel in channels_list:
        if channel == "defaults":
            channel = "anaconda"
        result = subprocess.run(["conda", "search", "-c", channel, package, package_sign, package_version], stdout=subprocess.PIPE)
        if package in result.stdout.decode():
            return channel
        
    # Search in PIP
    if search_pypi(package, package_sign, package_version):
        return "pip"

    return None

"""
    # Separate packages into Conda and pip lists
    conda_packages = []
    pip_packages = []
    for package in packages:
        repo = search_package(package)
        if repo is None:
            print(f"Package {package} not found in any repository.")
            continue

        if repo == "pip":
            pip_packages.append(package)
        else:
            conda_packages.append(package)

    # Install Conda packages
    for package in conda_packages:
        subprocess.run(["conda", "install", "--yes", "-c", "conda-forge", package], check=True)

    # Install pip packages
    for package in pip_packages:
        subprocess.run(["pip", "install", package], check=True)
"""


if __name__ == "__main__":
    #project_folder_name = unzip_starter_project_repo()
     
    #requirements = parse_requirements(project_folder_name)
    
    #channels_list = get_channels()
    #print(channels_list)
    
    #search_pypi(package, package_sign, package_version)
    releases_list = search_pypi("requests", "==", "2.31.0")
    print(releases_list)
    """
    env_list = get_envs()
    while True:
        env_name = input("Enter Environment Name: ")
        if env_name not in env_list:
            create_conda_env(str(env_name))
            print(f"Environment '{env_name}' has been created.")
            break  # Exit the loop
        else:
            print(f"Environment '{env_name}' already exists. Please enter a different environment name.")
"""

    """
    for requirement in requirements:
        package, package_sign, package_version = requirement
        repo = search_package(package, package_sign, package_version)
        if repo is None:
            print(f"Package {package} not found in any repository.")
            continue
        if repo == "pip":
            subprocess.run(["pip", "install", package], check=True)
        else:
            subprocess.run(["conda", "install", "--yes", "-c", "conda-forge", package], check=True)
    """