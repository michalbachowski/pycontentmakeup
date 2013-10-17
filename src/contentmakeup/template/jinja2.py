#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.template import Processor
from jinja2 import Environment


class Jinja2(Processor):

    def activate(self):
        self.env = Environment()

    def extensions(self):
        return ('jinja2',)

    def compile(self, template):
        tpl = self.env.from_string(template)
        return tpl.render
