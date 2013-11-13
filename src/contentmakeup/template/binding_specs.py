#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pinject import BindingSpec
from contentmakeup.template import ProcessorInterface


class TemplateBindingSpec(BindingSpec):

    def configure(self, bind):
        for plugin in ProcessorInterface.plugins:
            bind(plugin.accepts, to_class=plugin)
