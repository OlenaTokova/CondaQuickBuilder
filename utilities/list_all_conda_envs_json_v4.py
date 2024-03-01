"""
This script lists all the conda environments and their packages.

It uses the `conda env list --json` command to get the list of environments in JSON format. 
For each environment, it uses the `conda list --prefix {env_path} --json` command to get the list of packages in the environment.

The script prints the name or path of each environment, followed by the list of packages in that environment.
"""

import json
import subprocess

# Get the list of environments in JSON format
envs_json = subprocess.check_output("conda env list --json", shell=True).decode()

# Parse the JSON output
envs = json.loads(envs_json)

# The 'envs' key in the JSON output contains the list of environments
for env_path in envs['envs']:
    # Get the list of packages in the environment in JSON format
    packages_json = subprocess.check_output(f"conda list --prefix {env_path} --json", shell=True).decode()
    
    # Parse the JSON output
    packages = json.loads(packages_json)
    
    print(f"Environment: {env_path}")
    for package in packages:
        print(f"{package['name']} {package['version']}")