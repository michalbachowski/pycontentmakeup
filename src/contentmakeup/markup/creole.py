#!/usr/bin/env python
# -*- coding: utf-8 -*-
from creole import creole2html
from contentmakeup.markup import ParserInterface


class Creole(ParserInterface):
    accepts = ('creole',)

    def parse(self, input_type, output_format, text):
        return creole2html(text)
