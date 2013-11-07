#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wikimarkup import parse
from contentmakeup.markup import ParserInterface


class Wiki(ParserInterface):
    accepts = ('wiki',)

    def parse(self, input_type, output_format, text):
        return parse(text)
