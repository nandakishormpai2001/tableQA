#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:58:22 2020

@author: abhijithneilabraham
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tableqa-abhijithneilabraham", # Replace with your own username
    version="0.0.1",
    author="Abhijith Neil Abraham, Fariz Rahman",
    author_email="abhijithneilabrahampk@gmail.com,farizrahman4u@gmail.com",
    description="Tool for querying natural language on tabular data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhijithneilabraham/tableQA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)