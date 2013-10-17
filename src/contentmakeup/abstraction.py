#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyevent import Listener, DispatcherAware


class HookHandler(Listener, DispatcherAware):
    """
    Abstract class for hook handlers
    """
    NAME_PATTERN = 'contentmakeup.hook.%s'

    def mapping(self):
        """
        Returns list of listeners to be attached to dispatcher.
        [(event name, listener, priority), (event name, listener, priority)]
        """
        return [(self.NAME_PATTERN.format(self.__class__.__module__.lower()),
            self.handle_event, 400)]


class TemplatePlugin(HookHandler):
    """
    Abstract class tof template plugins
    """
    NAME_PATTERN = 'contentmakeup.template.plugin.%s'


class MarkupParser(object):
    """
    Abstract class for markup parser
    """

    def mime_types(self):
        """
        Returns set of mime types that are handled by this class
        """
        raise NotImplementedError("Provide list of allowed mime types")

    def parse(self, text):
        """
        Returns given text parsed

        :param    text: string to be parsed
        :type     text: string
        :returns: string -- parsed text
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide markup parsing mechanism")


class TemplateProcessor(object):
    """
    Abstract Template class
    """

    def process(self, template, args):
        """
        Processes template using given arguments.

        :param    template: template string
        :type     template: string
        :param    args: arguments to be used within template
        :type     args: dict
        :returns: string -- compiled template
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide template processor")


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
