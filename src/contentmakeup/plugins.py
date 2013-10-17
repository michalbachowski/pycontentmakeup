#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect
import importlib
import itertools
import os
import sys


class PluginLocator(object):

    def __call__(self):
        """
        Locates plugin using built in strategy

        :returns: iterator -- iterator with plugins to instantinate
        """
        raise NotImplementedError()


class PluginLocatorPath(PluginLocator):
    def __init__(self, paths, filter=None):
        self.paths = set(paths)
        if filter is None:
            filter = lambda x: True
        self.is_valid = filter
        self.cached = None

    def __call__(self):
        """
        Loads a set of plugins at the given path.

        Arguments:
        plugin_path - the OS path to look for plugins at.
        instance - classes of this instance will be returned
        """
        if self.cached is None:
            self.cache = self.locate_plugins()
        return self.cache

    def locate_plugins(self):
        out = []
        for path in self.paths:
            out.append(self.find_plugins_in_path(path))
        return itertools.chain.from_iterable(out)

    def find_plugins_in_path(self, path):
        plugin_dir = os.path.realpath(path)

        plugins = []
        for filename in os.listdir(plugin_dir):
            plugins.append(self.find_plugins_in_file(path, filename))
        return itertools.chain.from_iterable(plugins)

    def find_plugins_in_file(self, path, filename):
        plugins = []
        name = self.prepare_module_name(path, filename)
        if name is None:
            return plugins

        mod = self.import_module(path, name)
        return itertools.ifilter(self.is_valid, inspect.getmembers(mod))

    def prepare_module_name(self, plugin_dir, item):
        if item.endswith(".py"):
            return item[:-3]
        if item.endswith(".pyc"):
            return item[:-4]
        if os.path.isdir(os.path.join(plugin_dir, item)):
            return item

    def import_module(self, path, name):
        """
        Imports module given as path to directory and module name

        :param    path: path to import module from
        :type     path: string
        :param    name: name of module
        :type     name: string
        :returns: object -- loaded module
        """
        sys.path.append(path)
        return importlib.import_module(name)


class PluginFilter(object):

    def __call__(self, obj):
        pass


class PluginFilterIsInstance(object):

    def __init__(self, instance):
        self.instance = instance

    def __call__(self, obj):
        return isinstance(obj, self.instance)


class PluginFilterAggregate(PluginFilter):

    def __init__(self):
        self.is_valid = []

    def append(self, filter):
        self.is_valid.append(filter)

    def __call__(self, obj):
        for is_valid in self.is_valid:
            if not is_valid(obj):
                return False
        return True


class PluginFactory(object):

    def create(self, plugin_name):
        pass


class PluginFactoryDummy(object):
    """
    Dummy factory class. Just instantinates objects without any configuration
    """

    def create(self, plugin_name):
        """
        Factory method. Instantinates new object from given class.
        Be default object is not configured.
        In real implementations factory should configure object using provided configuration.

        :param    configuration: configuration to be used to configure object
        :type     configuration: dict
        :returns: object
        """
        return plugin_name()
