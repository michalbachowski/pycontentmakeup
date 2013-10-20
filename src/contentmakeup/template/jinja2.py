#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.template import ProcessorInterface
from jinja2 import Environment


class Jinja2(ProcessorInterface):

    def activate(self):
        self.env = Environment()

    def extensions(self):
        return ('jinja2',)

    def compile(self, template):
        tpl = self.env.from_string(template)
        return tpl.render
