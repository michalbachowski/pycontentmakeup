#!/usr/bin/env python
# -*- coding: utf-8 -*-
import markdown2
from contentmakeup.markup import ParserInterface


class Markdown(ParserInterface):

    def extensions(self):
        return ('md', 'markdown')

    def parse(self, text):
        return markdown2.markdown(text)
