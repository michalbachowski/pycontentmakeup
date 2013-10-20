#!/usr/bin/env python
# -*- coding: utf-8 -*-
import markdown2
from contentmakeup.markup import ParserInterface


class Markdown(ParserInterface):

    def accepts(self):
        return ('md', 'markdown')

    def parse(self, input_type, output_format, text):
        return markdown2.markdown(text)
