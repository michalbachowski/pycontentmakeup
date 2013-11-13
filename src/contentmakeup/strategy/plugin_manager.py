#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import product
from collections import defaultdict
from contentmakeup.strategy import StrategyInterface
from contentmakeup.template import ProcessorInterface
from contentmakeup.markup import ParserInterface


class PluginManager(StrategyInterface):
    """Manager for template and markup plugins"""
    subject = ("template_manager", "markup_manager")

    def __init__(self, object_graph):
        """Object initialization

        Arguments:
            :param    object_graph: instance of service locator
            :type     pinject.object_graph
        """
        self._plugins = {'markup': None, 'template': None}
        self._object_graph = object_graph

    def configure(self, plugin_type):
        """Configures plugins"""
        if self._plugins[plugin_type] is not None:
            return
        self._plugins[plugin_type] = defaultdict(dict)
        if 'template' == plugin_type:
            plugins = ProcessorInterface.plugins
        elif 'markup' == plugin_type:
            plugins = ParserInterface.plugins
        else:
            raise RuntimeError('Incorrect plugin_type "{}"'.format(plugin_type))
        for plugin in plugins:
            for (accepts, outputs) in product(plugin.accepts, plugin.outputs):
                self._plugins[plugin_type][accepts][outputs] = plugin

    def markup(self, input_type, output_format):
        """Returns markup parser for given input_type and output_format

        Arguments:
            :param    input_type: content type to process
            :type     input_type: str
            :param    output_format: type to output data in
            :type     output_format: str
        :returns      instance of plugin
        :raises:      KeyError -- in case of not having plugin for given
                                    (input, output) pair
        """
        return self.__call__('markup', input_type, output_format)

    def template(self, input_type, output_format):
        """Returns template processor for given input_type and output_format

        Arguments:
            :param    input_type: content type to process
            :type     input_type: str
            :param    output_format: type to output data in
            :type     output_format: str
        :returns      instance of plugin
        :raises:      KeyError -- in case of not having plugin for given
                                    (input, output) pair
        """
        return self.__call__('template', input_type, output_format)

    def __call__(self, plugin_type, input_type, output_format):
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
        self.configure(plugin_type)
        return self._object_graph.provide(\
                        self._plugins[plugin_type][input_type][output_format])
