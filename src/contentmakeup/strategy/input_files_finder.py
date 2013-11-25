#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# Python stdlib
#
import sys

##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class InputFilesFinder(StrategyInterface):
    subject = ('input_files_finder',)

    def __call__(self, files):
        return self._find_source(files)

    def _find_source(self, files):
        if files is None:
            return sys.stdin
        if len(files) == 1 and '-' == files[0]:
            return sys.stdin
        return files
