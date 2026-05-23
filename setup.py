'''
The setup.py file is an essential part of any Python project that is 
intended to be packaged and distributed. 
It is used to provide metadata about the project and 
to specify the dependencies that are required for the project to run.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirement() -> List[str]:
    '''
    this function will return the list of requirements
    '''
    requirement_list: List[str] = []
    try:
        with open('requirements.txt') as file:
            #Read lines from the file
            lines= file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and e- . 
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
       print("requirements.txt file not found")
    
    return requirement_list

setup(
    name="Network Security Project",
    version="0.0.1",
    author="Ryan Febrianto",
    author_email="ryanjecarygmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)
