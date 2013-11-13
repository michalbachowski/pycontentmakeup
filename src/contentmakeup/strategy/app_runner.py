#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# Python stdlib
#
import sys

##
# library modules
#
from contentmakeup.strategy import StrategyInterface


class AppRunner(StrategyInterface):
    subject = ('app_runner',)

    def __init__(self, content_parser, metadata_extractor, template_discovery, \
            template_renderer, config, merger, input_reader, format_discovery, \
            output_writer):
        self.parse_content = content_parser
        self.extract_metadata = metadata_extractor
        self.render_template = template_renderer
        self.discover_template = template_discovery
        self.discover_format = format_discovery
        self.read_input = input_reader
        self.write_output = output_writer
        self.config = config
        self.merge = merger

    def __call__(self, input_path, output_path, default_output_format):
        input_format = self.discover_format(input_path)
        output_format = self.discover_format(output_path, \
                                                        default_output_format)
        content = self.read_input(input_path)
        (metadata, raw_content) = self.extract_metadata(content, input_format)
        config = self.merge(metadata, self.config)
        template_file = self.discover_template(config)
        parsed_content = self.parse_content(raw_content, input_format, \
                                                                output_format)
        rendered_content = self.render_template(parsed_content, config, \
                                                template_file, output_format)
        self.write_output(output_path, rendered_content)
        return rendered_content

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass