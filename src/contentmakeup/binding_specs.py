#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# pinject
#
from pinject import BindingSpec

##
# config merging
#
from pycomber import merger
from pycomber.configuration import ConfigurationImmutable
from pycomber.strategies import MergeNone
from pycomber.value_objects import ImmutableDict


class AppBindingSpec(BindingSpec):
    """Configuration specification for pinject"""

    def __init__(self, config):
        self.config = config
        self.object_graph = None

    def add_object_graph(self, object_graph):
        self.object_graph = object_graph
        return self

    def provide_merger(self):
        ConfigurationImmutable()(merger)
        NoneType = type(None)
        types = (list, dict, set, tuple, ImmutableDict, frozenset)
        merger.set_strategy(MergeNone(merger), NoneType, types)
        merger.set_strategy(MergeNone(merger), types, NoneType)
        return merger

    def provide_object_graph(self):
        return self.object_graph

    def provide_config(self, plugin_loader):
        if 'plugins' in self.config:
            plugin_loader(self.config['plugins'])
        return self.config
