#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class InputReader(StrategyInterface):
    subject = ('input_reader',)

    def __call__(self, input_path):
        with open(input_path) as f:
            return f.read()
