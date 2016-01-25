# -*- coding: utf-8 -*-
#
# Copyright (C) Translate House and contributors.
#
# This file is a part of the PyLIFF project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

"""Python XLIFF object
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='pyliff',
    version='0.0.1',
    description='Python XLIFF object',
    long_description="Python XLIFF object",
    url='https://github.com/phlax/pyliff',
    author='Ryan Northey',
    author_email='ryan@synca.io',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL3',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='python xliff',
    install_requires=[
        'lxml'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True)
