#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pinject import BindingSpec
from contentmakeup.strategy import StrategyInterface


class StrategyBindingSpec(BindingSpec):

    def configure(self, bind):
        for plugin in StrategyInterface.plugins:
            for subject in plugin.subject:
                bind(subject, to_class=plugin)
