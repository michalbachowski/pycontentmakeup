#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.template import ProcessorInterface
from jinja2 import Environment


class Jinja2(ProcessorInterface):

    def __init__(self):
        self.env = Environment()

    def accepts(self):
        return ('jinja2',)

    def compile(self, input_type, output_format, template):
        tpl = self.env.from_string(template)
        return tpl.render
