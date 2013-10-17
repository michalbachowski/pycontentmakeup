#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yapsy.IPlugin import IPlugin


class Processor(IPlugin):
    """
    Abstract template processor class
    """

    def extensions(self):
        """
        Returns list of supported file extensions
        """
        raise NotImplementedError("Provide list of supported file extensions")


    def compile(self, template):
        """
        Compiles given template

        :param    template: template string
        :type     template: string
        :returns: callable -- callable that when called with arguments dict will render template
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide template compiler")
