#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yapsy.IPlugin import IPlugin


class Parser(IPlugin):
    """
    Abstract class for markup parser
    """

    def extensions(self):
        """
        Returns set of supported file extensions
        """
        raise NotImplementedError("Provide list of supported file extensions")

    def parse(self, text):
        """
        Returns given text parsed

        :param    text: string to be parsed
        :type     text: string
        :returns: string -- parsed text
        :raises:  NotImplementedError
        """
        raise NotImplementedError("Provide markup parsing mechanism")
