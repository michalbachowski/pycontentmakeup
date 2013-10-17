#!/usr/bin/env python
# -*- coding: utf-8 -*-





>>> import yaml
>>> test = "foo=1 bar=2 baz='123'"
>>> yaml.dump(test)
"foo=1 bar=2 baz='123'\n...\n"
>>> import shlex
>>> s = 'key1=1234 key2="string with space" key3="SrtingWithoutSpace"'
>>> print dict(token.split('=') for token in shlex.split(s))
{'key3': 'SrtingWithoutSpace', 'key2': 'string with space', 'key1': '1234'}
>>>
