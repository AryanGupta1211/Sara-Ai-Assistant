from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    try:
        with open('requirements.txt', 'r') as f:
            return [line.strip() for line in f if line.strip() and line.strip()!='-e .']
    except FileNotFoundError:
        raise FileNotFoundError("requirements.txt file not found. Please create it with the necessary dependencies.")

setup(
    name='sara-ai-bot',
    version='0.1.0',
    author='Aryan Gupta',
    packages=find_packages(),
    install_requires=get_requirements(),
)