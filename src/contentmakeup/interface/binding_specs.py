#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from itertools import chain

##
# pinject
#
from pinject import BindingSpec


class CliBindingSpec(BindingSpec):

    def __init__(self, args):
        self.args = args

    def provide_config(self, configuration_parser):
        return configuration_parser(self.args.config)

    def provide_files(self):
        if len(self.args.file) == 1 and '-' == self.args.file[0]:
            inp = sys.stdin
        else:
            inp = self.args.file
        return map(lambda line: list(chain(line.strip().split(' '), \
                                                            ['-']))[0:2], inp)

    def provide_output_format(self):
        return self.args.output_format
