#!/usr/bin/env python
# -*- coding: utf-8 -*-
from contentmakeup.markup import ParserInterface


class Pandoc(ParserInterface):
    """Pandoc base markup parser. See https://github.com/jgm/pandoc"""
    accepts = ('native', 'json', 'markdown', 'markdown_strict', \
                'markdown_phpextra', 'markdown_github', 'textile', 'docbook', \
                'rst', 'html', 'opml', 'mediawiki', 'haddock', 'latex')
    outputs = ('native', 'json', 'plain', 'markdown', 'markdown_strict', \
                'markdown_phpextra', 'markdown_github', 'rst', 'html', \
                'html5', 'latex', 'beamer', 'context', 'man', 'mediawiki', \
                'textile', 'org', 'texinfo', 'opml', 'docbook', \
                'opendocument', 'docx', 'rtf', 'epub', 'epub3', 'fb2', \
                'asciidoc', 'slidy', 'slideous', 'dzslides', 'revealjs')

    def parse(self, input_type, output_format, text):
        raise NotImplementedError('Pandoc.parse is not implemented')
