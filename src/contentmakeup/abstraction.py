#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyevent import Listener, DispatcherAware


class TemplatePlugin(HookHandler):
    """
    Abstract class tof template plugins
    """
    NAME_PATTERN = 'contentmakeup.template.plugin.%s'


class GenericFactory(object):
    """
    Generic factory class. Allows to instantinate objects from given class
    """

    def __init__(self, cls):
        """
        Object constructor.

        :param    cls: class to be instantinated on demand
        :type     cls: callable
        :returns: None
        """
        self.cls = cls

    def __call__(self, configuration):
        """
        Factory method. Instantinates new object from given class.
        Be default object is not configured.
        In real implementations factory should configure object using provided configuration.

        :param    configuration: configuration to be used to configure object
        :type     configuration: dict
        :returns: object
        """
        return self.cls()
