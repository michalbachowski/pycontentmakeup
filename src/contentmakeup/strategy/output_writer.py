#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# Python stdlib
#
import sys

##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class OutputWriter(StrategyInterface):
    subject = ('output_writer',)

    def __call__(self, path, content):
        if '-' == path:
            sys.stdout.write(content)
        else:
            with open(path, 'w+') as output:
                output.write(content)
