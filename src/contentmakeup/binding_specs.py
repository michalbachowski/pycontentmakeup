#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspd import MountPoint
from pinject import BindingSpec
import six


@six.add_metaclass(MountPoint)
class BindingSpecMountPoint(BindingSpec):
    """
    Rendez vous point for binding specs
    """
    pass
