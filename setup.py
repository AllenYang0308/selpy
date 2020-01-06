from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="ezselenium",
    version="0.1.0",
    author="Allen Yang",
    author_email="musasi.yang@gmail.com",
    description="Python Framework.",
    license="MIT",
    url="https://github.com/AllenYang0308",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Chinese',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: NLP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
            'selenium>=3.141.0',
            'pandas>=0.20.0',
            'numpy>=1.14.0'
    ],
    zip_safe=True,
    package_data={
        'binary': ['*.*', 'firefox/*'],
        'driver': ['*.*']
    },
)
