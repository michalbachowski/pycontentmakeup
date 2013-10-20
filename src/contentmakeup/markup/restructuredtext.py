#!/usr/bin/env python
# -*- coding: utf-8 -*-
from docutils.core import publish_parts
from contentmakeup.markup import ParserInterface


class ReStructuredText(ParserInterface):

    def accepts(self):
        return ('restructured', 're')

    def parse(self, input_type, output_format, text):
        return publish_parts(text, writer_name='html')['html_body']
