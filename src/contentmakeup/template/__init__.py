#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class ProcessorInterface(object):
    """
    Abstract template processor class
    """

    def accepts(self):
        """
        Returns list of supported template types

        :returns: set -- set of supported template types
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide list of supported template types")

    def outputs(self):
        """
        Returns set of supported output fromats

        :returns: set -- set of supported output formats. Defaults to 'html'
        """
        return ('html',)

    def compile(self, input_type, output_format, template):
        """
        Compiles given template

        :param    input_type: name of template type
        :type     input_type: string
        :param    output_format: name of output format
        :type     output_format: string
        :param    template: template string
        :type     template: string
        :returns: callable -- callable that when called with arguments dict will render template
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide template compiler")
