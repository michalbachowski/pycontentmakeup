#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.template import ProcessorInterface
from mako.template import Template


class Mako(ProcessorInterface):

    def accepts(self):
        return ('mako',)

    def compile(self, input_type, output_format, template):
        return Template(template).render
