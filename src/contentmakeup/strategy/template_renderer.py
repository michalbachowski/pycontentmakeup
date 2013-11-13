#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.strategy import StrategyInterface


class TemplateRenderer(StrategyInterface):
    """Class describes strategy for extracting metadata"""
    subject = ('template_renderer',)

    def __init__(self, format_discovery, template_manager, input_reader):
        self.template_manager = template_manager
        self.discover_format = format_discovery
        self.read_input = input_reader
        self._compiled = {}

    def __call__(self, content, config, template_file, output_format):
        return self._get_compiled(template_file, output_format)({'content': \
                                                    content, 'config': config})

    def _get_compiled(self, template_file, output_format):
        if template_file not in self._compiled:
            self._compiled[template_file] = self._compile(template_file, \
                                                          output_format)
        return self._compiled[template_file]

    def _compile(self, template_file, output_format):
        template_type = self.discover_format(template_file)
        return self.template_manager.template(template_type, \
            output_format).compile(template_type, output_format, \
            self.read_input(template_file))
