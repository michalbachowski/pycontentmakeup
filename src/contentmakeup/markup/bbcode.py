#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bbcode
from contentmakeup.markup import ParserInterface


class Bbcode(ParserInterface):

    def accepts(self):
        return ('bb', 'bbcode')

    def parse(self, input_type, output_format, text):
        return bbcode.render_html(text)
