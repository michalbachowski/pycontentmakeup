#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# own modules
#
from contentmakeup.strategy import StrategyInterface

##
# binding specs modules
from contentmakeup.binding_specs import BindingSpecMountPoint

##
# pinject (dependency injection container)
#
from pinject import new_object_graph, BindingSpec


class AppInitializer(StrategyInterface):
    subject = ('app_initializer',)

    class _Helper(object):

        def __init__(self, app_runner):
            self.app_runner = app_runner

    def __init__(self, config, plugin_loader):
        self.config = config
        self._object_graph = None
        if 'plugins' in config:
            plugin_loader(config['plugins'])

    def __call__(self, files):
        with self.object_graph.provide(AppInitializer._Helper).app_runner as \
            runner:
            map(runner, files)

    @property
    def object_graph(self):
        if self._object_graph is None:
            self._object_graph = self.init_object_graph(self.config)
        return self._object_graph

    def init_object_graph(self, config):
        self.app_binding_spec = AppBindingSpec(config)
        specs = [bs() for bs in BindingSpecMountPoint.plugins]
        specs.append(self.app_binding_spec)
        object_graph = new_object_graph(binding_specs=specs)
        self.app_binding_spec.add_object_graph(object_graph)
        return object_graph


class AppBindingSpec(BindingSpec):
    """Configuration specification for pinject"""

    def __init__(self, config):
        self.config = config
        self.object_graph = None

    def add_object_graph(self, object_graph):
        self.object_graph = object_graph
        return self

    def provide_object_graph(self):
        return self.object_graph

    def provide_config(self, plugin_loader):
        return self.config
