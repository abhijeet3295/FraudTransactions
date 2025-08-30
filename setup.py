from setuptools import find_packages,setup
from typing import List

HYPE_DOT_E='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPE_DOT_E in requirements:
            requirements.remove(HYPE_DOT_E)

    return requirements


setup(
name='FraudTransactios',
version='0.0.1',
author='Abhijeet Singh',
author_email='abhijeet71004@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)