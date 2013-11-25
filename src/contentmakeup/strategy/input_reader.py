#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class InputReader(StrategyInterface):
    subject = ('input_reader',)

    def __init__(self, input_path_discovery):
        self.discover_path = input_path_discovery

    def __call__(self, input_path):
        with open(self.discover_path(input_path)) as f:
            return f.read()
