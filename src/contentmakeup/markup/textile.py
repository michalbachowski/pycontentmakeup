#!/usr/bin/env python
# -*- coding: utf-8 -*-
import textile
from contentmakeup.markup import ParserInterface


class Textile(ParserInterface):
    accepts = ('textile',)

    def parse(self, input_type, output_format, text):
        return textile.textile(text)
