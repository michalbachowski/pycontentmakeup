#!/usr/bin/env python
# -*- coding: utf-8 -*-
import markdown2
from contentmakeup.markup import Parser


class Markdown(Parser):

    def extensions(self):
        return ('md', 'markdown')

    def parse(self, text):
        return markdown2.markdown(text)
