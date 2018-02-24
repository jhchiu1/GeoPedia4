from setuptools import setup, find_packages


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    packages=find_packages(exclude=["build.*"]),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "project4 = project4.main:main"
        ]
    })
