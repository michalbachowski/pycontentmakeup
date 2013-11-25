#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# Python stdlib
#
import os

##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class InputPathDiscovery(StrategyInterface):
    subject = ('input_path_discovery',)

    def __init__(self, config):
        self.base_path = config['base_path']
        self.config_paths = config['directories']

    def __call__(self, input_path):
        if not self._is_known_path(input_path):
            raise RuntimeError("Path '%s' should begin with one of: %s" \
                                    % (input_path, self.config_paths.values()))
        return os.path.join(self.base_path, input_path)

    def _is_known_path(self, input_path):
        for path in self.config_paths.values():
            if input_path.startswith(path):
                return True
        return False
