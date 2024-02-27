"""
<COPILOT-PROMPT>
<PROMPT-DATE: 2024-02-23>
I want to determine programmatically if an existing local conda environment is a good fit to use as a starting point to clone for a new project.

Give me step-by-step instructions and detailed code for a fast way to do this. I want to be able to run the code and see the results in my terminal.
"""

import subprocess
import json

def get_conda_packages(environment_name):
    command = f"conda list -n {environment_name} --json"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
    else:
        return json.loads(output)

def extract_package_names(packages):
    return [package['name'] for package in packages]

def compare_packages(project_requirements, package_names):
    missing_packages = [package for package in project_requirements if package not in package_names]

    if missing_packages:
        print(f"The following packages are missing in the conda environment: {missing_packages}")
    else:
        print("The conda environment has all the required packages.")

#########################################
# replace with your actual requirements
project_requirements = ['numpy', 'pandas', 'scikit-learn']  

environment_name = "webscrapers"

# Replace 'your_environment_name' with the name of your conda environment
packages = get_conda_packages(environment_name)
print(packages)


if __name__ == "__main__":
    # Replace 'your_environment_name' with the name of your conda environment
    packages = get_conda_packages('environment_name')
    package_names = extract_package_names(packages)

    # Replace with your actual requirements
    project_requirements = ['numpy', 'pandas', 'scikit-learn']  

    compare_packages(project_requirements, package_names)