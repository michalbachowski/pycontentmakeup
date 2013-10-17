#!/usr/bin/env python
# -*- coding: utf-8 -*-
import textile
from contentmakeup.markup import Parser


class Textile(Parser):

    def extensions(self):
        return ('textile',)

    def parse(self, text):
        return textile.textile(text)
