#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.strategy import StrategyInterface

##
# pyspd modules (plugin locators)
#
from pyspd.locator.aggregate import LocatorAggregate
from pyspd.locator.dir import LocatorDir
from pyspd.locator.file import LocatorFile
from pyspd.locator.module import LocatorModule


class PluginLoader(StrategyInterface):
    """Class describes strategy for extracting metadata"""
    subject = ('plugin_loader',)

    def __init__(self):
        self.locator_types = {'dir': LocatorDir, 'file': LocatorFile, \
            'module': LocatorModule}

    def __call__(self, config):
        locator = LocatorAggregate()
        for (type_name, type_locator) in self.locator_types.items():
            if type_name not in config:
                continue
            for path in config[type_name]:
                locator.append(type_locator(path))
        locator()
