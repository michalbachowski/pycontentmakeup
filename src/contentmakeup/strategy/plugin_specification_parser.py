#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shlex
from contentmakeup.strategy import StrategyInterface


class PluginSpecificationParser(StrategyInterface):
    """Class describes strategy for parsing plugin content"""
    subject = ('plugin_specification_parser',)


    def __call__(self, data):
        return dict(token.split('=') for token in shlex.split(data))
