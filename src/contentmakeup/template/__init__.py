#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class ProcessorInterface(object):
    """
    Abstract template processor class
    """
    accepts = tuple()
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
