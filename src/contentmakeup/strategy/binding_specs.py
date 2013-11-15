#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.binding_specs import BindingSpecMountPoint
from contentmakeup.strategy import StrategyInterface


class StrategyBindingSpec(BindingSpecMountPoint):

    def configure(self, bind):
        for plugin in StrategyInterface.plugins:
            for subject in plugin.subject:
                bind(subject, to_class=plugin)
