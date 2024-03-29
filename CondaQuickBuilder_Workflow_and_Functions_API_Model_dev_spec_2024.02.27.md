##### CondaQuickBuilder Workflow and Functions API Model
## This document extracts functions identified in document: 
## CondaQuickBuilder_Project_Description-2024.02.17-1507h 

Defines "function flow" matching the workflow defined as "detailed steps".

Created On: 2024.02.21 2206h
Updated On: 2024.02.27 1853h
(this markdown file replaced the YAML file with the same name.)

TODO: Prompt Sequence: refine steps below to prepare them for Copilot or ChatGPT prompts.

# LOGIC SEQUENCE
# TODO: get logic clearer and more organized for main:
# 1. Unzip the starter project repository
# 1b. Clone the starter project repository directly from GitHub
# 1c. Determine whether there is a environments.yml file or a requirements.txt file
# 1d. If there is an environments.yml file, use it to create the environment
# 1e. If there is a requirements.txt file, use it to create the environment
# 1f. If there is a Poetry spec (pyproject.toml) instead of a environments.yml or requirements.txt file, ask the user what to do next, or use the Poetry spec to create the environment.   
#    Version 1.0+ of CondaQuickBuilder will not support Poetry, but it can be added in a future version.
# 3. Parse the requirements file

# 2. Plan to use latest version of Python BY DEFAULT, UNLESS the new project package requires an older version
# 2b. Alert the user that latest version of Python will be used.  Ask thes if they want to use a different version, if it is not specified in the requirements file


# 4. Get the list of channels used in the conda configuration (if available)
# 5. Get the list of environments availble locally
# 6. Create a new environment
# 7. Install the packages in the environment
# 8. Save the versions of the packages (?) to a file

1) project_name = "CondaQuickBuilder"

2) Project_description = "CondaQuickBuilder is an automated tool designed to accelerate the setup of new projects by building a new Conda environment from an existing project repository package."

List of likely functions known as needed: 

3) TODO: SETUP CODE INSTRUMENTATION: 
    configure logging:
    start logging: 

4) TODO: User enters target repo: https://github.com/streamlit/streamlit-hello/

5) TODO: function: fetch_remote_repo()

6) TODO: function: get_new_project_name()
        """get name from zip file"""
        return project_name

7) DONE: function: unzip_starter_project_repo()

8) function: scan_project_modules()
    """Scans modules in fetched remote repo to get  names of dependent packages."""  
    return_value: py_dependencies_set

9) function: scan_existing_envs()
        return:  current_env_dependencies_set

        scan (ALL?) our local pre-existing virtual environments 

        function: scan_existing_env()
            current_env_dependencies_set
    
10) function: measure_env_fit() ???? 
        take set (lists, tuple or other?) of environment packages 
        do package "match and score" operation 
        identify "best" fit of current environments' dependency trees,
        return the one(s) that match.

11) function: repo_search(): 

    Do conditional searches for packages in the following order:

        If all packages are found in conda-forge, use those and stop searching.

        a) search_conda_forge()
                return: conda_forge_search_results
        
        else if not all packages are found in conda-forge, search anaconda.

        b) search_anaconda() 
            return: anaconda_search_results
        
        else if not all packages are found in anaconda, search pypi.
        
        c) search_pip()
            return: pip_search_results

    return conda_forge_search_results, anaconda_search_results, pip_search_results

12) function: build_repos_lists()

13) set conda_channel_priority = ["conda-forge", "anaconda", "pypi"]

14) create Python functions (or separate script commands?) needed to execute the environment build steps.

    a) function: create_conda_core_env() 

        "conda create --new {get_new_project_name()} --channel conda-forge python conda pip"

        if conda create throws "warning prompt" to upgrade conda:

            handle_conda_update_prompt() 

        if conda create throws "conda update warning prompt" to upgrade conda:

        set flag for "conda update warning"

          handle "globally" (system-wide)
          handle "locally"  (locally in the new conda environment)
          postpone conda update (not_now)

    b) function: conda_activate() 
            call "conda activate {new_env}"

        if handle conda update "locally"  (locally in the new conda environment)

            call function: update_local_conda_env():
                
                which executes terminal command "call conda update conda --name {new_env} --channel conda-forge"

    c) call function search_conda_forge() to get list of packages from conda_forge_search_results()

    d) function: install_conda_forge_packages_list() 

        call "conda install -c conda-forge conda_forge_search_results"

            return: success (or failure)

            function: handle_installation_exceptions()
                pass (TBD)
                return: success (or failure)

    e) function: install_anaconda_packages_list() 

        call "conda install -c anaconda anaconda_search_results"

        function: handle_installation_exceptions()

    f) function: install_pip_packages() 

          call "pip install pip_packages_list"

          function: handle_installation_exceptions()


    g) monitor installation process, and handle exceptions: 
        Types of Exceptions: 
            "package not found", 
            "specified version not found"
            "{XYZ} build version not available for the installed version of Python"

            " XYZ build version not available for} package version installed {


            [conda install -c anaconda (???)]
            [conda install -c conda-OTHER

    h) pip install ... all remaining packages that are NOT available in conda format
