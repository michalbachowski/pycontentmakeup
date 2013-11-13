#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# Python stdlib
#
import os

##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class FormatDiscovery(StrategyInterface):
    subject = ('format_discovery',)

    def __call__(self, input_path, default=None):
        ext = os.path.splitext(input_path)[1][1:]
        if len(ext) == 0:
            return default
        return ext
