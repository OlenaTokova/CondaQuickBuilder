Initial Workflow Description: 
1. Load a requirements.txt
2. Create file main.py
3. Create function for Load requirements.txt
4. Function for parse_requirements() put module, version_sign, version in array 
5. Function for creating Conda env
6. ## Check-in: After Run - Type: Environment Name. Make a test: conda install -n {env.name} requests. This command allows you install packages in {env.name}. We use it for function istallation packages in other environment.
7. Create a loop to test existing env and in case "if env not exist, create new".
8. Create a function for unzip our pakages. After, function return name folder of unzipped project. 
