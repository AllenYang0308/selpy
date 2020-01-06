from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name='ezselenium',
    version='0.1.0',
    license='BSD',
    author='Allen Yang',
    author_email='allen.yang@ezprice.com.tw',
    maintainer='IDV team',
    description='',
    py_modules=['ezselenium'],
    packages=['binary', 'driver'],
    package_data={
        'binary': ['*.*', 'firefox/*'],
        'driver': ['*.*']
    },
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'selenium>=3.141.0'
    ],
)
