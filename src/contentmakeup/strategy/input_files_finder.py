#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# Python stdlib
#
import sys
from itertools import chain

##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class FilesFinder(StrategyInterface):
    subject = ('files_finder',)

    def __call__(self, files):
        return map(lambda line: list(chain(line.strip().split(' '), \
                                        ['-']))[0:2], self._find_source(files))

    def _find_source(self, files):
        if files is None:
            return sys.stdin
        if len(files) == 1 and '-' == files[0]:
            return sys.stdin
        return files
