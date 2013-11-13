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
        'contentmakeup.markup', 'contentmakeup.interface',
        'contentmakeup.strategy'],
    package_dir={'': 'src'})
