import io
import os
import re

from setuptools import find_packages
from setuptools import setup

__version__ = '0.0.1'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gwwapi",
    version=__version__,
    url="https://github.com/global-water-watch/gww-api",
    license='MIT',

    author="Jurian Beunk",
    author_email="jurianbeunk@gmail.com",

    description="A python package for using the Global Water Watch API",
    long_description_content_type="text/markdown",
    long_description=long_description,

    packages=find_packages(exclude=('tests',)),

    install_requires=[
        "geopandas",
        "pandas",
        "requests",
        "shapely",
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)