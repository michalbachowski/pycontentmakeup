#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from contentmakeup.template import ProcessorInterface
from mako.template import Template


class Mako(ProcessorInterface):
    accepts = ('mako',)

    def compile(self, input_type, template):
        return Template(template).render
