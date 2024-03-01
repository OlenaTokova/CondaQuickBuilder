"""
This script lists all the conda environments and their packages.

It uses the `conda env list` command to get the list of environments. For each environment, it checks if a name is available.
If a name is available, it uses the `conda list --name {env_name}` command to get the list of packages in the environment.
If only a path is available, it uses the `conda list --prefix {env_path}` command to get the list of packages.

The script prints the name or path of each environment, followed by the list of packages in that environment.
"""

import subprocess

# Get the list of environments
envs = subprocess.check_output("conda env list", shell=True).decode().splitlines()

# Skip the first 3 lines and the last line, which don't contain environments
for env in envs[3:-1]:
    # Split the line into words
    words = env.split()
    
    # If the line contains a name, it's the first word; otherwise, it's None
    env_name = words[0] if words else None
    
    # The path is always the last word on the line
    env_path = words[-1]
    
    # If the name is available, use it to get the list of packages
    if env_name:
        packages = subprocess.check_output(f"conda list --name {env_name}", shell=True).decode()
    else:
        # If only the path is available, use it to get the list of packages
        packages = subprocess.check_output(f"conda list --prefix {env_path}", shell=True).decode()
    
    print(f"Environment: {env_name or env_path}")
    print(packages)