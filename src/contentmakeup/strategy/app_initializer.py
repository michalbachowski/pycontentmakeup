#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# library modules
#
from contentmakeup.strategy import StrategyInterface

##
# binding specs modules
from contentmakeup.strategy.binding_specs import StrategyBindingSpec
from contentmakeup.template.binding_specs import TemplateBindingSpec
from contentmakeup.binding_specs import AppBindingSpec

##
# pinject modules (dependency injection container)
#
from pinject import new_object_graph


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

    def __call__(self, files, default_output_format):
        with self.object_graph.provide(AppInitializer._Helper).app_runner as \
            runner:
            for (input_path, output_path) in files:
                runner(input_path, output_path, default_output_format)

    @property
    def object_graph(self):
        if self._object_graph is None:
            self._object_graph = self.init_object_graph(self.config)
        return self._object_graph

    def init_object_graph(self, config):
        self.app_binding_spec = AppBindingSpec(config)
        specs = [self.app_binding_spec, StrategyBindingSpec(), \
                 TemplateBindingSpec()]
        object_graph = new_object_graph(binding_specs=specs)
        self.app_binding_spec.add_object_graph(object_graph)
        return object_graph
