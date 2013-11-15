#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# own modules
#
from contentmakeup.strategy import StrategyInterface

##
# pycomber (object merging)
#
from pycomber import merger
from pycomber.configuration import ConfigurationImmutable


class ObjectMerger(StrategyInterface):
    subject = ('object_merger',)

    def __init__(self):
        ConfigurationImmutable()(merger)
        self._merger = merger

    def __call__(self, merge_from, merge_to):
        """Merges given instances merge_from and merge_to.
        Creates new instances during merge process.

        Arguments:
            :param    merge_from: merge from this object
            :type     merge_from: object
            :param    merge_to: merge to this object
            :type     merge_to: object
        :returns: object
        :raises: TypeError
        """
        return self._merger(merge_from, merge_to)
