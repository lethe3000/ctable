#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='colortable',
    py_modules=['colortable'],
    version='0.3',
    description='Print colorful(256) tables for terminal with built-in themes',
    author='lethe3000',
    author_email='lethe30003000@gmail.com',
    url='https://github.com/lethe3000/ctable',
    download_url='https://github.com/lethe3000/ctable/tarball/0.3',
    keywords=['table', 'terminal', 'color'],
    classifiers=[],
    install_requires=['tabulate==0.7.7'],
)
