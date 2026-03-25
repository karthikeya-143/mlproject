from setuptools import find_packages, setup

def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.read().splitlines()

        requirements = [
            req.strip()
            for req in requirements
            if req.strip() and not req.startswith("-e")
        ]

    return requirements

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)