#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import product
from collections import defaultdict
from contentmakeup.strategy import StrategyInterface
from contentmakeup.template import ProcessorInterface
from contentmakeup.markup import ParserInterface


class PluginManager(object):
    """Manager for plugin"""

    def __init__(self, object_graph, mount_point):
        """Object initialization

        Arguments:
            :param    object_graph: instance of service locator
            :type     object_graph: pinject.object_graph
            :param    mount_point: class that holds plugins list
            :type     mount_point: object
        """
        self._mount_point = mount_point
        self._plugins = None
        self._object_graph = object_graph

    def configure(self):
        """Configures plugins"""
        if self._plugins is not None:
            return
        self._plugins = defaultdict(dict)
        for plugin in self._mount_point.plugins:
            for (accepts, outputs) in product(plugin.accepts, plugin.outputs):
                self._plugins[accepts][outputs] = plugin

    def __call__(self, input_type, output_format):
        """Returns plugin for given input_type and output_format

        Arguments:
            :param    plugin_type: plugin type to load: manager or template
            :type     plugin_type: str
            :param    input_type: content type to process
            :type     input_type: str
            :param    output_format: type to output data in
            :type     output_format: str
        :returns      instance of plugin
        :raises:      KeyError -- in case of not having plugin for given
                                    (input, output) pair
        """
        self.configure()
        return self._object_graph.provide(\
                        self._plugins[input_type][output_format])


class TemplateManager(PluginManager, StrategyInterface):
    """Manager for template renderers"""
    subject = ("template_manager",)

    def __init__(self, object_graph):
        """Object initialization

        Arguments:
            :param    object_graph: instance of service locator
            :type     pinject.object_graph
        """
        PluginManager.__init__(self, object_graph, ProcessorInterface)


class MarkupManager(PluginManager, StrategyInterface):
    """Manager for markup parsers"""
    subject = ("markup_manager",)

    def __init__(self, object_graph):
        """Object initialization

        Arguments:
            :param    object_graph: instance of service locator
            :type     pinject.object_graph
        """
        PluginManager.__init__(self, object_graph, ParserInterface)
