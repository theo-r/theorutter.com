---
title: Getting Started with Python - an Opinionated Guide
date: "2023-08-01T22:12:03.284Z"
description: "Getting started with Python"
---

1. Download Python

To start, you need to download Python onto your machine. My preferred way to do this is directly via
the python.org website. Head to https://www.python.org/downloads/ and find your desired version of Python for the operating system you are working with. In my case I'll download the first option offered to me which happens to be 3.11.4 for MacOS.
The download includes an installer which will guide you through the necessary steps to install Python.
The installer may provide the option to update the PATH environment variable to include the location of the newly installed Python program - if it does make sure the option is selected.
<!-- todo screenshot of the python installer -->

At this point you should be able to open up the terminal of your choice and execute the command `python` (or `python3` on MacOS/Linux) to start up a Python shell directly from the command line. If this doesn't work the most likely issues are that Python was not installed successfully, or that it has not been added to the PATH.
<!-- todo screenshot of python in the terminal -->

2. Set up a virtual environment

Now that Python is installed, navigate to the directory you will be using to develop your project and create a virtual environment. Different projects may require different packages or versions of Python, so virtual environments are used to create isolated environments for each project. To create a virtual environment, execute the command `python3 -m venv .venv`. After executing this command you will notice a directory named `.venv` has been created. To activate the virtual environment, run `source .venv/bin/activate` on MacOS or `.venv/Scripts/activate` on Windows. The terminal will indicate that a virtual 
environment is being used. Now whenever a library is installed it will be associated with the current virtual environment.

3. Install packages and set up requirements.txt

Depending on the demands of your project you will likely have to install libraries from the internet
to provide specific capabilities for your Python programs. To install libraries you can use the `pip` package manager.
For example, you may wish to make http requests in your project using the popular `requests` module. Run `pip install requests`
to install the library. At any time you can use the `pip freeze` command to view the libraries that have been installed
in your virtual environment. 

To create a bill of materials for your Python project with a list of the libraries that
are required to run the projects programs, create a file called `requirements.txt` in your project directory. The requirements
file can be used to install all the included libraries in one go using the command `pip install -r requirements.txt`. Pin
the versions of each library to ensure that users of the project are using the correct versions of the necessary libraries.

4. Set up VSCode

Integrated Development Environments or IDEs are programs dedicated to creating, editing and running software seamlessly.
My preference is VSCode which can be downloaded from https://code.visualstudio.com/download. After downloading and installing
VSCode make sure that the `code` command is added to your PATH variable. This will allow you to navigate to a project directory
and run the command `code .` to open VSCode in that directory. Next install the `Python` extension for code highlighting and
additional features.

5. Use Jupyter Notebooks

Install the `jupyter` library and create a file with the `.ipynb` suffix in your project directory. Now when you open
this file in VSCode you should be presented with an interactive notebook interface for creating and running Python code
cells. Make sure your virtual environment is being used as the kernel so that all your installed libraries are available
to the code running in the notebook.