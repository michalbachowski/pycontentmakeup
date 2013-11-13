#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.strategy import StrategyInterface


class MetadataExtractor(StrategyInterface):
    """Class describes strategy for extracting metadata"""
    subject = ('metadata_extractor',)

    def __init__(self, yaml_loader):
        self._yaml_loader = yaml_loader

    def __call__(self, content, content_type):
        """Performs strategy action

        Arguments:
            :param    content: data to extract metadata from
            :type     content: str
            :param    content_type: type of given content
            :type     content_type: str
        :returns: object -- returned value from strategy
        """
        metadata = ''
        raw_content = content
        if content.startswith('---'):
            (dummy, metadata, raw_content) = content.split('---', 2)
        return (self._yaml_loader(metadata), raw_content)
