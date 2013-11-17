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

    def compile(self, input_type, template):
        """
        Compiles given template

        :param    input_type: name of template type
        :type     input_type: string
        :param    template: template string
        :type     template: string
        :returns: callable that when called with dict will render template
        :rtype:   callable
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide template compiler")
