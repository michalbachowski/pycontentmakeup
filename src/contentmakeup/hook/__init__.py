#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyevent import Listener, DispatcherAware
from pyspd import MountPoint
import six


@six.add_metaclass(MountPoint)
class HookInterface(Listener, DispatcherAware):
    """
    Abstract class for hook handlers
    """

    def mapping(self):
        """
        Returns list of listeners to be attached to dispatcher.
        [(event name, listener, priority), (event name, listener, priority)]
        """
        return [('contentmakeup.hook.', self.handle_event, 400)]
