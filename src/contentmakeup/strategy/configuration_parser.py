#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.strategy import StrategyInterface

class ConfigurationParser(StrategyInterface):
    """Strategy for parsing configuration"""
    subject = ("configuration_parser",)

    def __init__(self, yaml_loader):
        self._yaml_loader = yaml_loader

    def __call__(self, path):
        return self.from_file(path)

    def from_file(self, path):
        with open(path, 'r') as f:
            return self.from_string(f.read())

    def from_string(self, data):
        out = self._yaml_loader(data)
        if out is None:
            return {}
        return out
