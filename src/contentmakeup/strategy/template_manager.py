#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.strategy import StrategyInterface
from contentmakeup.template import ProcessorInterface


class TemplateManager(StrategyInterface):
    """Manager for template renderers"""
    subject = ('template_manager',)

    def __init__(self, object_graph):
        """Object initialization

        Arguments:
            :param    object_graph: instance of service locator
            :type     object_graph: pinject.object_graph
        """
        self._mount_point = ProcessorInterface
        self._plugins = None
        self._object_graph = object_graph

    def configure(self):
        """Configures plugins"""
        if self._plugins is not None:
            return
        self._plugins = {}
        for plugin in self._mount_point.plugins:
            for accepts in plugin.accepts:
                self._plugins[accepts] = plugin

    def __call__(self, input_type):
        """Returns plugin for given input_type and output_format

        Arguments:
            :param    plugin_type: plugin type to load: manager or template
            :type     plugin_type: str
            :param    input_type: content type to process
            :type     input_type: str
        :returns      instance of plugin
        :raises:      KeyError -- in case of not having plugin for given
                                    (input, output) pair
        """
        self.configure()
        return self._object_graph.provide(self._plugins[input_type])
