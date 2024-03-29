##### CondaQuickBuilder Workflow and Functions API Model
## This document extracts functions identified in document: 
## CondaQuickBuilder_Project_Description-2024.02.17-1507h 

Defines "function flow" matching the workflow defined as detailed steps.

Created On: 2024.02.21 2206h
(this markdown file replaced the YAML file with the same name.)

TODO: Prompt Sequence: refine steps below to prepare them for Copilot or ChatGPT prompts.

1) For this project, the name is "CondaQuickBuilder"

2a) CondaQuickBuilder is an automated tool designed to accelerate the setup of new projects by building a new Conda environment from an existing project repository package.

Below are the list of likely functions needed that are known thus far: 

3) SETUP CODE INSTRUMENTATION: 
    configure logging:
    start logging: 

4) User enters target repo: https://github.com/streamlit/streamlit-hello/

4a)    function: fetch_remote_repo()

4b) function: get_new_project_name()
        """get name from zip file"""
        return project_name

5) function: unzip_starter_project_repo()

6) function: scan_project_modules()
    return_value: py_dependencies_set

7) function: scan_existing_env()
            current_env_dependencies_set
    
8) function: measure_env_fit() ???? 

9) function: repo_search(): 

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

10) function: build_repos_lists()

11) set conda_channel_priority = ["conda-forge", "anaconda", "pypi"]

12) create Python functions (or separate script commands?) needed to execute the environment build steps.

    a) function: create_conda_core_env() 

        "conda create --new {get_new_project_name()} --channel conda-forge python conda pip"

        if conda create throws "warning prompt" to upgrade conda:

    a2) handle_conda_update_prompt() 

        if conda create throws "conda update warning prompt" to upgrade conda:

        set flag for "conda update warning"

          handle "globally" (system-wide)
          handle "locally"  (locally in the new conda environment)
          postpone conda update (not_now)

    b) function: conda_activate() 
            "conda activate {new_env}"

          handle conda update "locally"  (locally in the new conda environment)

     b2)  function: update_conda_locally():
           
           "call conda update conda --name {new_env}"

    c) call search_conda_forge() to get conda_forge_search_results

    d) function: install_conda_forge_packages_list() 

        call "conda install -c conda-forge conda_forge_search_results"

            return: success (or failure)

            function: handle_installation_exceptions()
                pass (TBD)
                return: success (or failure)

    e) function: install_anaconda_packages_list() 

        call "conda install -c anaconda anaconda_search_results"

        function: handle_installation_exceptions()

    d) function: install_pip_packages() 

          call "pip install pip_packages_list"

          function: handle_installation_exceptions()




    1) monitor installation process, and handle exceptions: 
        Types of Exceptions: 
            "package not found", 
            "specified version not found"
            "{XYZ} build version not available for the installed version of Python"

            " XYZ build version not available for} package version installed {


            [conda install -c anaconda (???)]
            [conda install -c conda-OTHER

        d) pip install ... all remaining packages that are NOT available in conda format
