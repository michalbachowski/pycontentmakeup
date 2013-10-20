#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class ParserInterface(object):
    """
    Abstract class for markup parser
    """

    def accepts(self):
        """
        Returns set of supported input types
        """
        raise NotImplementedError("Provide list of supported input types")

    def outputs(self):
        """
        Returns set of supported output fromats

        :returns: set -- set of supported output formats. Defaults to 'html'
        """
        return ('html',)

    def parse(self, input_type, output_format, text):
        """
        Returns given text parsed

        :param    input_type: name of input type
        :type     input_type: string
        :param    output_format: name of output format
        :type     output_format: string
        :param    text: string to be parsed
        :type     text: string
        :returns: string -- parsed text
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide markup parsing mechanism")
