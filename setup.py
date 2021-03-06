from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="ACI Apps",
    version="1.0.0",
    author="Chris O",
    author_email="cober91130@gmail.com",
    description="Used for Cisco ACI Apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cober2019/ACIApps",
    packages=find_packages(),
    install_requires=("flask", "ipaddress", "requests", "flask_migrate"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6')
