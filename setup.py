#!/usr/bin/env python

from setuptools import setup

DEPENDENCIES = [
    'click',
    'click-spinner',
    'requests',
]

setup(
    name = 'greynoise',
    version = '1.0.0',
    description = 'Python library and command-line utility for Greynoise (https://www.greynoise.io)',
    author = 'John Matherly',
    author_email = 'jmath@shodan.io',
    url = 'http://github.com/achillean/greynoise/tree/master',
    packages = ['greynoise'],
    entry_points = {'console_scripts': ['greynoise = greynoise.__main__:main']},
    install_requires = DEPENDENCIES,
    keywords = ['security', 'network'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
