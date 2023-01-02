.. _readme:

=======================================
gwwapi: Global Water Watch for Python
=======================================

|pypi| |python|

Installation 
--------------------------------
``pip install gwwapi``

Usage
--------------------------------
The package contains 2 modules:

*   client: allows a user to make requests from the Global Water Watch API

``from gwwapi import client``

*   utils: reshape raw data into convenient format (Pandas and GeoPandas)

``from gwwapi import utils``    

.. |pypi| image:: https://img.shields.io/pypi/v/gwwapi.svg?style=flat
  :target: https://pypi.org/project/gwwapi/
  :alt: PyPI   
  
.. |python| image:: https://img.shields.io/pypi/pyversions/gwwapi
   :alt: PyPI - Python Version
