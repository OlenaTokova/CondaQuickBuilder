"""
Use conda list --name {env_name} to list the packages in a specific environment without activating it. 
This can be much faster, especially if you have many environments. 
"""

import subprocess

# Get the list of environments
envs = subprocess.check_output("conda env list", shell=True).decode().splitlines()

# Skip the first 3 lines and the last line, which don't contain environments
for env in envs[3:-1]:
    # The name of the environment is the first word on the line
    env_name = env.split()[0]
    
    # Get the list of packages in the environment
    packages = subprocess.check_output(f"conda list --name {env_name}", shell=True).decode()
    
    print(f"Environment: {env_name}")
    print(packages)
    
