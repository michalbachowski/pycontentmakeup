#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


# monkey patch os.link to force using symlinks
import os
del os.link

setup(name='PyContentMakeUp',
    url='https://github.com/michalbachowski/pycontentmakeup',
    version='0.1.0',
    description='Python content parser and generator',
    license='New BSD License',
    author='Michał Bachowski',
    author_email='michal@bachowski.pl',
    packages=['contentmakeup', 'contentmakeup.hook', 'contentmakeup.template',
        'contentmakeup.markup'],
    package_dir={'': 'src', 'hook': 'src/hook', 'template': 'src/template',
        'markup': 'src/markup'},
    install_requires=['PyPromise==1.1.0', 'pyspd==0.1.0', 'six==1.3.0',
        'PyYAML>=3.10.0', 'pyspd=>0.2.0'])
