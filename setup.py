from setuptools import setup, Extension
from setuptools import find_packages
from setuptools.config import read_configuration

import mypackage

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(
        name="mypackage",
        version=mypackage.__version__,
        description="MYPACKAGE: My Demo Package",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Debanga Raj Neog",
        author_email="debanga88@gmail.com",
        url="https://github.com/debanga/demo_package",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
        install_requires=["numpy>=1.18.5"],
        scripts=[
            'scripts/greetings.py',
           ]
    )