'''Key purposes of setup.py:
Package metadata: Provides information about the package, including its name, version, author, and license.
Dependency management: Specifies the dependencies required by the package, such as other Python packages or libraries.
Build and installation: Defines the steps needed to build and install the package, including compiling C extensions, copying files, and running tests.
Distribution: Generates distribution files (e.g., source archives, wheel packages) for easy distribution and installation.'''

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    # This function will return list of requirements
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        # -e . initiates the setup.py automatically when requirements is called
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    # some metadata about the project
    name='ML_Project',
    version='0.0.1',
    author='Aniket',
    author_email='aniketmalpure28@gmail.com',
    packages=find_packages(),  # This is basically search for the folder having __init__.py to build package
    install_requires=get_requirements('requirements.txt')
)