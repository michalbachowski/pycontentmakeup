#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
# python std lib
import sys
import os
import argparse

from contentmakeup.interface.binding_specs import CliBindingSpec

##
# pinject modules (dependency injection container)
#
from pinject import new_object_graph, copy_args_to_public_fields

##
# possible support for argcomplete
try:
    import argcomplete
except ImportError:
    argcomplete = None


def argparser():
    """ Prepares argparse instance PYTHON_ARGCOMPLETE_OK """
    # argument parser
    parser = argparse.ArgumentParser(description='Command line utility for contentmakeup')

    parser.add_argument('-c, --config', dest='config', type=str, \
            default=os.path.join(os.getcwd(), 'config.yaml'), \
            help='Path to configuration file')

    parser.add_argument('file', type=str, default='-', nargs='+', \
        help="""Name of input file in format:
        "INPUT_FILENAME OUTPUT_FILENAME"
        (please notice dublequotes around pair of file names)
        If OUTPUT_FILENAME is ommited or set to "-" the STDOUT will be used.

        If file is specified as '%(default)s' names of input file
        will be read from STDIN - each (input, output) pair in single line""")

    # verbosity
    parser.add_argument('-q, --quiet', dest='quiet', action='store_true')
    return parser


def get_object_graph(args):
    specs = [CliBindingSpec(args)]
    object_graph = new_object_graph(binding_specs=specs)
    return object_graph


class Runner(object):

    @copy_args_to_public_fields
    def __init__(self, app_initializer, args, files_finder):
        app_initializer(files_finder(args.file))
        self.exit_code = 0


def load_default_modules():
    from contentmakeup.strategy.configuration_parser import ConfigurationParser
    from contentmakeup.strategy.yaml_loader import YamlLoader
    from contentmakeup.strategy.app_initializer import AppInitializer
    from contentmakeup.strategy.plugin_loader import PluginLoader
    from contentmakeup.strategy.files_finder import FilesFinder


def main():
    """ main method """
    parser = argparser()
    if argcomplete:
        argcomplete.autocomplete(parser)
    args = parser.parse_args()

    return get_object_graph(args).provide(Runner).exit_code


if '__main__' == __name__:
    ##
    # default strategies are loaded only when script is executed as executable
    load_default_modules()
    sys.exit(main())
