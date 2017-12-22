#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# pyobjc-core pyobjc osx
# python3-xlib linux
# also apt-get scrot python3-tk python3-dev
"""

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


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
    install_requires=[
      'pyautogui'
    ],
    extras_require={
        'docs': ['releases']
    },
    include_package_data=True
)
