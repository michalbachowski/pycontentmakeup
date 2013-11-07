#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
from itertools import product
from collection import defaultdict
import six


@six.add_metaclass(MountPoint)
class ProcessorInterface(object):
    """
    Abstract template processor class
    """
    accepts = None
    outputs = ('html', )

    def compile(self, input_type, output_format, template):
        """
        Compiles given template

        :param    input_type: name of template type
        :type     input_type: string
        :param    output_format: name of output format
        :type     output_format: string
        :param    template: template string
        :type     template: string
        :returns: callable that when called with dict will render template
        :rtype:   callable
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide template compiler")


class Manager(object):
    """Template processors manager"""

    def __init__(self, object_graph):
        """Object initialization

        Arguments:
            :param    object_graph: instance of service locator
            :type     pinject.object_graph
        """
        self._processors = None
        self.object_graph = object_graph

    def _configure(self):
        """Configures processors (lazy loads)"""
        if self._processors is not None:
            return
        self._processors = defaultdict(dict)
        for plugin in ProcessorInterface.plugins:
            for (accepts, outputs) in product(plugin.accepts, plugin.outputs):
                self._processors[accepts][outputs] = plugin

    def get_processor(self, input_type, output_format):
        """Returns processor for given input_type and output_format

        Arguments:
            :param    input_type: content type to process
            :type     input_type: str
            :param    output_format: type to output data in
            :type     output_format: str
        :returns      ProcessorInterface -- instance of processor
        :raises:      KeyError -- in case of not having processor for given
                                    (input, output) pair
        """
        self._configure()
        return self._object_graph.provide(\
                                    self._processors[input_type][output_format])
