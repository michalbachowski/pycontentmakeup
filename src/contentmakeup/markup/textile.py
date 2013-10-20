#!/usr/bin/env python
# -*- coding: utf-8 -*-
import textile
from contentmakeup.markup import ParserInterface


class Textile(ParserInterface):

    def extensions(self):
        return ('textile',)

    def parse(self, text):
        return textile.textile(text)
