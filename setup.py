#!/usr/bin/env python3

from setuptools import setup

setup(
    name='classify',
    packages=['classify'],
    include_package_data=True,
    python_requires=">=3.9.*",
    install_requires=['netaddr'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['classify=classify.main:main'],
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ],
)
