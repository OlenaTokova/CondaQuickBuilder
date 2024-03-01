"""
This script lists all the conda environments and their packages.

It uses the `conda env list --json` command to get the list of environments in JSON format. 
For each environment, it uses the `conda list --prefix {env_path} --json` command to get the list of packages in the environment.

The script creates a pandas DataFrame with the environment, package name, and package version, 
and then stores this DataFrame in a SQLite database.
"""

import json
import subprocess
import pandas as pd
import sqlite3

# Create a list to store the data
data = []

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
    
    for package in packages:
        # Add the environment, package name, and package version to the data list
        data.append([env_path, package['name'], package['version']])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Environment', 'Package', 'Version'])

# Create a connection to the SQLite database
conn = sqlite3.connect('conda_envs.db')

# Store the DataFrame in the SQLite database
df.to_sql('packages', conn, if_exists='replace')

# Close the connection to the SQLite database
conn.close()