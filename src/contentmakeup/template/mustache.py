#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import partial
import pystache
from contentmakeup.template import ProcessorInterface


class Mustache(ProcessorInterface):

    def extensions(self):
        return ('mustache',)

    def compile(self, template):
        return partial(pystache.render, pystache.parse(template))
