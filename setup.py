#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name = "longerusername",
    version = "0.4",
    packages = find_packages(),
    zip_safe = False,
)
