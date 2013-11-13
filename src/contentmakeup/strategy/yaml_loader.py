#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yaml import load
from contentmakeup.strategy import StrategyInterface


class YamlLoader(StrategyInterface):
    """Class describes strategy for loading YAML data"""
    subject = ('yaml_loader',)

    def __call__(self, data):
        """Performs strategy action

        Arguments:
            :param    data: data to be dumped
            :type     data: str
        :returns: object -- returned value from strategy
        """
        return load(data)
