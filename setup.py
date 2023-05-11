import re
import pathlib
from setuptools import setup, find_packages

# project dirs 
package_source = pathlib.Path("tgjson")

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

VERSION_FILE = package_source/"__init__.py"
getversion = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSION_FILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError(f"Unable to find version string in {VERSION_FILE}.")

setup(
    name='tgjson',
    version=new_version,    
    description='A example Python package',
    url='https://github.com/ffernandoalves/tgjson',
    author='Fernando Ribeiro Alves',
    author_email='fernandoribeiro889@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements,
    keywords=["json", "pyrogram"],
    python_requires='>=3.10',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)