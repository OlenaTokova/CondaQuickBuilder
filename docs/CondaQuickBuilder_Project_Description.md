
## End-to-end AI-Powered Project Example: ORIGINAL MESSAGE (LEARNING ASSIGNMENT)

	This version of the original file was copied from:
		G:\My Drive\JOB SEARCH\MassHire WIOA\NTAI training materials\Automated_Conda_project.txt
		which was Updated: 2024.02.09-1400h

	Updated at 4:26 PM.
	C:\Users\Staff\Desktop\CondaQuickBuilder_Project_Description-2024.02.12-1514h.md
	   Title:  "Automated Conda Environment Builder Tool"

	   Purpose: Develop a useful utility to help accelerate new projects by automating the process of building a conda virtual environment from a project repository zipfile.

	This is a terse technical project plan.  The development process is a WIP.

	We are using this as a more complete example of using AI to follow a defined development workflow.  

	When the tool is done everyone can use the tool and post it as a portfolio project (if you show up and contribute in some way).

	We want to finish the entire production tool and exercise in less than < 5 hours. 

	Attached is the project definition file (so far) with the business requirements and workflow steps.

	Requirements specifications have been drafted first.  It is far enough along now to feed it into Copilot or ChatGPT to generate working examples.  

	No code has been generated yet.  

	Next Steps:

	Please look it over and provide your input to it to clarify it for yourself

	Try running it through Copilot and ChatGPT to test what comes out.  

	We will continue with this on Friday and/or Saturday.

	We will use both Copilot and ChatGPT to generate the code to compare the process and outputs.  We could try different ChatGPT versions, (and maybe Bard?) to compare quality and effort required to finalize it.

	I am interested to see your results.

	Tasks:


	team project example for Automated Conda Environment Builder Tool

	Rich Lysakowski
	Attachments
	Feb 8, 2024, 8:01 AM (1 day ago)
	to Elena, Hi, me, Rocio, Monzia, nagla, Pankaj, Biraja, Cesar, Abigail, Anil, Mona, Herbert, Vincent
	
###################################################################################  

## Project Description: Develop Automated [conda] Project Environment Builder Product

### Start Date:  2024.02.07
### End Date:    2024.02.12

### Project Participants:
    Olena Tokova, Hilary Shea, Nadia Stoyanova, Rocio Calle, 
    Monzia Moodie, Biraja Dash, Pankaj Verma, Cesar Anderson, Anil Naik, others

### Lead Scribe: Rich Lysakowski
### Testers

### Project Workflow to create a tool with Copilot in VScode 
    Workflow Methodology (Steps to create a tool)
        
    6D Agile Software Develop - [iDeate], Define, Design, Develop, Debug, Document, Deliver

### Project Purpose: Learn step-by-step process of building and delivering products using AI.

    The CondaQuickBuilder "product" is a vehicle chosen to forward the learning process.  
    
    This project was chosen because it is sufficiently detailed to require some requirement from the original vision, through implementation and delivery in a team context.  

### Learning Goals and Deliverables: 

    TODO: distinquish between skills and knowledge deliverables and software deliverable(s)

    Skills Deliverables: TODO: 
    Main Product Deliverable: End-to-end Automated Tool to generate Python script that builds a new conda environment from a project repository package

    TODO: refine and combine all parts of this section into a coherent and concise description: 
    a) Step through 6D-Agile Product Define-to-Deliver Process 
    b) Create a production version of the tool that automatically sets up working conda environment when starting a new development project. 
    c) Provide a useful tool for people to use to accelerate their work.
    d) Post-project goal stretch goal: articulate requirements for a "meta-tool" to automate build similar scope tools 

#############################################################

#### 6-D Agile Concise Process Overview: 
    0) name the baby to be delivered
	1) articulate 1-paragraph description that defines the "business problem".
	2) describes technical solution to solve business problem
    3) articulate project scope, requirements, and constraints
    4) follow 6D Agile phases 
   

### Business Problem Statement: 
    In the fast-paced world of software development, setting up new project environments can be a time-consuming and error-prone process. Developers often need to manually create a new Conda environment and install necessary dependencies based on the contents of a project repository package. This manual process can lead to inconsistencies across different environments and slow down the overall development process, reducing productivity and efficiency. Doing this quickly requires expertise and experience as well as methodology that is informed by experience. The issue of broken environments leading to the waste of time.

		TODO: ***Make the business problem description more concise if possible.***
		
### Technical Solution: CondaQuickBuilder 
    
    QuickBuilder will addresses this business problem by automating the process of setting up a new Conda environment.  It accepts a project repository package as input, extracts the necessary dependencies, and generates a Python script that uses Conda commands to create a new environment and install these dependencies. This tool can also automatically run the generated script to create the environment. With detailed logging and error handling, CondaQuickBuilder ensures transparency and reliability in the environment setup process. 

	This solution design goals will include not only to save time and reduce errors, but also ensure consistency across different environments, and thereby accelerate the software development process.

		TODO: *** Make this Technical Solution description more concise, (if possible).***

    TODO: Notes about actions to take: 
		To make requirements actionable for the purposes of code generation, PRECISELY represent the objects and functions of your code: 
            A) clearly identify the nouns/objects and the verbs/functions, 
            B) adjective/metrics/measures are usually used to define product characteristics like the "ilties" for performance, usability, maintainability, reliability, etc.
        


## Product Define Phase
	## Product Name: CondaQuickBuilder
	
	## Product Description: CondaQuickBuilder is an automated tool designed to accelerate the setup of new projects by building a new Conda environment from an existing project repository package.  The goal is to reduce the time and manual effort required to manually set up project environments, thus increasing productivity and efficiency for developers.  
    The tool output will be a Python script for user to generate the conda environment.  


### Brainstorming on Names - (create a catchy project title: "CondaQuickBuilder")

	Asked Copilot for possible suggestions gave the following: 

	# CondaEnvBuilder
	# AutoCondaEnv
	# EnvZipAutomator
	# CondaEnvZipper
	# ProjectEnvCreator
	# CondaQuickStart
	# ZipToEnv
	# CondaEnvAccelerator
	# RapidEnvBuilder
	# CondaEnvAutomator
	
	Original name was Automated [conda] Project Environment Builder.  
	It was changed to CondaQuickBuilder.

### Define Main Features:

	### Main Features are named described below. 

	### Input: Accepts a project repository package (zip file) as input.
	
	### Environment Extraction: Extracts the project repository and identifies the necessary dependencies from files like requirements.txt or environment.yml.
	
	### Script Generation: Generates a Python script with commands to create a new Conda environment and install the necessary dependencies within the conda environment.
	
	### Automatic Environment Creation: Option to automatically run the generated script to create the environment.
	
	### Logging: Provides detailed logs of the process for debugging and transparency.
	
	### Error Handling: "Gracefully" logs warnings, errors, and successful operations
	
	### Reporting: Reports progress and provides "useful" (user-actionable) warnings and error messages.

### Define Product Requirements (from main features):

	*** TODO: Make these descriptions very concise without losing any technical xplanation

	### Input Handling: Accept a project repository package (zip file) as input.
	
	### Environment Extraction: Extract the project repository and identify necessary ependencies.
	
	### Script Generation: Generate a Python script with Conda commands for creating a ew environment and installing dependencies.
	
	### Environment Creation: Provide an option to automatically run the generated cript to create the environment.
	
	### Logging: Provide detailed logs of the process.
	
	### Error Handling: Handle errors gracefully and provide useful error messages.
	
	### Testing: Include thorough testing, with unit tests for each module and ntegration tests for the whole system.
	
	### Documentation: Provide comprehensive documentation, including usage instructions nd explanations of each module.


	##### Required Technologies:
	
		## Python: The main language for developing the tool.
			
		## Conda: The package and environment management system.
			
		## pytest: The testing framework for Python (use this for the development version only)

    ### REQUIREMENTS SCOPE TODO: move scope statements to this section
    #### WHAT'S IN-SCOPE
    #### WHAT'S OUT-OF-SCOPE

###### TODO: Project Scope: 
    TODO: this needs to be refined into clear version scope statements: 

    The scope of the CondaQuickBuilder project includes the design, development, and testing of a tool that automates the process of setting up a new Conda environment from a project repository package. The tool will be able to extract necessary dependencies from the package, generate a Python script with Conda commands to create a new environment and install the dependencies, and optionally run the generated script. The project also includes the development of detailed logging and error handling mechanisms.

    TODO: Clarify these scope constraints, make them concise:

        #### Version 1: 

		###### Project Constraints:
			
			###### Technical Constraints: The tool is designed to work with Conda and Python. 

            It may not work with other package managers or programming languages without modifications.

            V1 conda environment manager and Pip python package managers
            V1.1 additional features 
			V2+ Javascript NPM, Bower, and other non-Python package managers

			###### Time Constraints: Depending on the project timeline, some features (like a graphical user interface or support for other package managers) may need to be deferred to future versions.
			
			###### Resource Constraints: The development of the tool depends on the availability of resources, including development tools and personnel. Any changes in these resources could impact the project timeline and deliverables.


##### Future Enhancements:

	## Additional Requirements TBD: Usability, testability...along with requirementand feature definition

	TODO: See these articles to learn more: 
	
		"The 7 Software “-ilities” You Need To Know"
		https://codesqueeze.com/the-7-software-ilities-you-need-to-know/

		"The Essential Qualities in Software Engineering - the 'ilities'"
		https://www.linkedin.com/pulse/essential-qualities-software-engineering

	## GUI: Develop a graphical user interface for easier usage.
	
	## Support for Other Package Managers: Extend the tool to support other packagmanagers like npm, ruby-on-rails, R, etc.
		
	## Custom Configuration: Allow end-users (both developers and regular users) tprovide custom configurations for environment setup.


	Search for pre-existing packages.
	Select the best-fitting package.
	Download the chosen package.
	Unzip it into a new project folder.
	Scan for Python dependencies.
	

### Define Project IMPLEMENTATION PLAN (Project Management) 

    This section defines the sequence of steps to implement Product BASED ON PRODUCT REQUIREMENT DEFINITIONS earlier.

	Implementation Steps:
		
	TODO: ***Question: Should these feature sets be implemented as separate modules?*** 

	## Setup Development Project: Set up a Python project with a good structure and ecessary configurations.
	
	## Develop Input Module: Develop a module to accept and validate the input zip file.
	
	## Develop Extraction Module: Develop a module to extract the zip file and identify ecessary dependencies.
	
	## Develop Script Generation Module: Develop a module to generate a Python script with onda commands for creating a new environment and installing dependencies.
	
	## Develop Environment Creation Module: Develop a module to run the generated script and reate the Conda environment.
	
	## Develop Logging Module: Develop a module to log the process details.
	
	## Develop Error Handling Module: Develop a module to handle errors and exceptions.
	
	## Testing: Write unit tests for each module and perform integration testing.
	
	## Documentation: Document the usage of the tool and each of its modules.
		


### Project Purpose: Create End-to-end Automated Tool to generate Python script that builds a new conda environment from a project repository package.

#### Setup Project Development Tools
    1) Open VSCode
    
	2) Create New Workspace with the Name for New Project
    
	3) Develop and flesh out "Project Description"



####### Design Phase

######## High-Level Design 
    High-level description of the workflow - What? how to download the best tool for your project, does not describe the exact code (except business reqs - must have env). 

######### Detailed Design: exactly how to use the environment, or the code: step by step, algorithm, pseudocode. 

########## PRODUCT Workflow - Define Detailed Steps: 

    2) Search for pre-existing packages that fit the bill
         Don't reinvent the wheel - find something already available that meets the requirements
    3) Select existing that meets the initial requirements
    4) Download the best fitting package

    4b) user-specifies project folder name - function: get_new_project_name()
    5) unzip the best fitting package into new project folder [with a user-specified name]
            function: unzip_starter_project_repo()
    6) scan the project folder to find the (unique) set of required Python package dependencies
            function: scan_project_modules()
            py_dependencies_set
    7) scan our local pre-existing virtual environments to see which fits the dependency tree the best.
            function: scan_existing_env()
            current_env_dependencies_set
    8) decide whether to use or clone a pre-existing virtual environment or create a new one?
        Does an existing environment have required "current enough" packages to stand up the project?
            function: measure_env_fit() ? 
    9) use "conda search" to see if each package dependency is available in conda-channel priority: 
            search function: 1) search_conda_forge(), 2) search_anaconda(), 3) search_pip()
            a) conda-forge     (set of packages IN conda-forge)
            b) anaconda        (set of packages NOT IN conda-forge, but anaconda)
            c) pip             (set of packages NOT IN (conda-forge OR anaconda)

    10) iterate over step 9 until all (new) packages and required versions are found
            a) build list of repos (conda-forge, anaconda, CONDA-OTHER, or pip) containing required versions 
                function: build_repos_lists()

    12) create Python functions (or separate script commands?) needed to execute the environment build steps.

        a) conda create "core" environment using as many conda-forge packages as possible
            Example: conda create -n new_env -c conda-forge python, conda, etc.

        b) conda activate new_env

        c) conda install -c conda-forge ... all the other packages
            [conda install -c anaconda (???)]
            [conda install -c conda-OTHER

        d) pip install ... all remaining packages that are NOT available in conda format

    13) Build final script to execute The 12 Steps 
    14) Test final script
    15) Deliver

##### Project Object Model: 
    new_project_dependency_set

    existing_env_package_set  - (for v1, assume we inquire about only one preexisting env)

    conda_forge_pkg_list
    anaconda_pkg_list
    pip_only_pkg_list

##### Functions API Model

    Extract functions identified above in Project Workflow - Define Detailed Steps: 

## Product Development Phase (TBD)

### **FEED PROJECT OVERVIEW, DETAILED DESIGN (WORKFLOW AND OBJECT MODEL)**

### **use the following (possibly redundant) text with the section above: "Project Workflow - Define Detailed Steps">>

    Create a Python program to sequentially search for a Python conda packages list provided by the user. 

    Use "conda search" for conda-only versions of packages in the "conda-forge" channel,

    Use "conda search" infor "anaconda" channel. 

    Build a list of the latest versions of packages is available in each repository (conda-forge, anaconda, pip), 

    Finally search pip for the remaining Python packages that do not have a current conda package, and build a Python function to install the remaining packages.

    Prioritize the installation commands:
        "conda install -c conda-forge" packages first 
        "conda install -c anaconda" packages next 
        "pip install <pip-only package names>"

    Critical "robustness" requirements:  
        Add fault-tolerance and error-checking, 
        Log process to a time-stamped file 

    Provide output report files as a markdown or HTML text file(s) for final lists of packages pulled and installed from conda-forge, anaconda, and pip.  

    Display final reports:
        In web browser (Markdown/HTML format). 
        In Notepad++ (Markdown format, for editing)



## Product Debug (test) Phase
    Get core functionality tested
    Enhance with important features missed earlier


## Product Document Phase

## Product Deliver Phase




# FOLLOW-ON PROJECT USING LANGCHAIN 

Purpose: Build Automated Tool for Building Tools
    A Lower-code forms-driven way to automate the process of building  tools and utilities using LLMs

MetaTool Creation Meta-Workflow:

This could be part of a suite of automated intelligent software "project accelerators". 
2024.02.08-Automated_Project_Conda_Env_Builder.md
Zoomed out of item.




### Define and Describe Project Purpose & Requirements
    1) create a catchy project title 
    2) articulate 1-paragraph description that:
        a) defines the "business problem"
        b) describes technical solution to solve business problem
    3) articulate project scrope, requirements, and constraints
