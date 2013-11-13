#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class StrategyInterface(object):
    """
    Abstract class for strategies

    :cvar subject: name of strategy to support
    :type subject: string
    """
    subject = tuple()

    def __call__(self, *args, **kwargs):
        """Performs strategy action

        :returns: object -- returned value from strategy
        """
        raise NotImplementedError("Implement strategy method")
