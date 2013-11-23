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


class OutputPathDiscovery(StrategyInterface):
    subject = ('output_path_discovery',)

    def __init__(self, config):
        self.config = config

    def __call__(self, input_path):
        path, filename = os.path.split(input_path)
        filebasename, ext = os.path.splitext(filename)
        return self.config['output_path'].format(filename=filebasename, \
                                        ext=self.config['output_format'])
