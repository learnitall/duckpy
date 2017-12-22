#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup.py installation file for duckpy.
"""

import os
from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


# If installing on READTHEDOCS then don't install pyautogui
if os.environ.get('READTHEDOCS') == 'True':
    install_reqs = []
else:
    install_reqs = ['pyautogui']


setup(
    name='duckpy',
    version='0.1',
    description='Duckyscript interpreter written in Python',
    long_description=readme(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Topic :: Education :: Testing',
        'Topic :: Security',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Software Development :: Testing'
    ],
    keywords='ducky duckyscript rubber ducky testing local python hak5',
    url='http://github.com/developforlizardz/duckpy',
    author='Ryan Drew',
    author_email='developforlizardz@gmail.com',
    license='mit',
    packages=['duckpy'],
    install_requires=install_reqs,
    extras_require={
        'docs': ['releases']
    },
    include_package_data=True
)
