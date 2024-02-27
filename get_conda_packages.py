import subprocess

def get_conda_packages(environment_name):
    command = f"conda activate {environment_name} && conda list"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
    else:
        return output.decode()


#########################################
# replace with your actual requirements
project_requirements = ['numpy', 'pandas', 'scikit-learn']  

environment_name = "webscrapers"

# Replace 'your_environment_name' with the name of your conda environment
packages = get_conda_packages(environment_name)
print(packages)
