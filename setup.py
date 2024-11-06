from typing import List

from setuptools import setup, find_packages

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    return de list of requirements
    :param file_path:
    :return:
    """
    requirements = []
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if line.startswith(HYPEN_E_DOT):
                continue
            requirements.append(line)
    return requirements

setup(
    name= 'randomArt',
    version= '0.0.1',
    author= 'Idriss Tafo',
    author_email= 'idrisstafo9@gmail.com',
    description= 'Random Art Generator',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)