#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial
import pystache
from contentmakeup.template import ProcessorInterface


class Mustache(ProcessorInterface):
    accepts = ('mustache',)

    def compile(self, input_type, output_format, template):
        return partial(pystache.render, pystache.parse(template))
