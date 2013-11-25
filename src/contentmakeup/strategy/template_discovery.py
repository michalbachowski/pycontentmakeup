#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from contentmakeup.strategy import StrategyInterface


class TemplateDiscovery(StrategyInterface):
    """Class describes strategy for discovering template"""
    subject = ('template_discovery',)

    def __call__(self, config):
        return os.path.join(config['directories']['templates'], \
                                                        config['template_file'])
