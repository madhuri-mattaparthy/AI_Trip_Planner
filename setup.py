from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        # Open and read the requirements.txt file
        with open("requirements.txt","r") as file:
            lines = file.readlines()
            
            for line in lines:
                req = line.strip()
                
                if req and req != "-e .":
                    requirement_list.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())

setup(
    name="AI-TRAVEL-PLANNER",
    version="0.0.1",
    author="Madhuri Mattaparthy",
    author_email="mmattaparthy4@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)