#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# pinject
#
from pinject import BindingSpec


class CliBindingSpec(BindingSpec):

    def __init__(self, args):
        self.args = args

    def provide_config(self, configuration_parser):
        return configuration_parser(self.args.config)

    def provide_args(self):
        return self.args
