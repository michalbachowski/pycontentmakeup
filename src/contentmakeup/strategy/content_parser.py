#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.strategy import StrategyInterface


class ContentParser(StrategyInterface):
    """Class describes strategy for extracting metadata"""
    subject = ('content_parser',)

    def __init__(self, config, markup_manager):
        self.config = config
        self.markup_manager = markup_manager

    def __call__(self, content, content_type, output_format):
        return self.markup_manager.markup(content_type, output_format).parse(\
                                        content_type, output_format, content)
