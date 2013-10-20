#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.template import ProcessorInterface


class Html(ProcessorInterface):

    def accepts(self):
        return ('html',)

    def compile(self, input_type, output_format, template):
        return lambda *args, **kwargs: template
