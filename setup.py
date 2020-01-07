from __future__ import print_function
from setuptools import setup
import sys

setup(
    name='ezselenium',
    version='0.1.0',
    license='BSD',
    author='Allen Yang',
    author_email='allen.yang@ezprice.com.tw',
    maintainer='IDV team',
    description='',
    packages=['ezselenium'],
    package_data={
        'ezselenium': ['*.*', 'firefox/*'],
    },
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'selenium'
    ],
)
