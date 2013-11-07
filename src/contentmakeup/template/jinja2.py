#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.template import ProcessorInterface
from jinja2 import Environment


class Jinja2(ProcessorInterface):
    accepts = ('jinja2',)

    def __init__(self):
        self.env = Environment()

    def compile(self, input_type, output_format, template):
        tpl = self.env.from_string(template)
        return tpl.render
