# -*- coding: utf-8 -*-
"""
@FileName: env
@Time: 2020/2/18 12:26
@Author: zhaojm

Module Description

"""

import codecs

from parser.parser import Parser
from prototype.prototype import ProtoType


class ENV(object):
    def __init__(self):
        self.modules = {}  # path: closure
        self.protos = {}

    def compile_file(self, filename):
        """

        """
        with codecs.open(filename, encoding='utf-8') as f:
            print('=' * 100)

            ast = Parser(filename, f.read()).parse_file()

            print('=' * 100)

            # print('ast.execute result: >>', ast.execute())

            print('=' * 100)

            proto = ProtoType(None, filename)
            proto.name = filename
            proto.env = self

            ast.to_bin(proto)

            print("proto-->>", proto)
            self.add_proto(filename, proto)

    def add_proto(self, filename, proto):
        self.protos[filename] = proto

    def get_proto(self, filename):
        return self.protos[filename]

    def set_module(self, path, closure):
        """

        """
        self.modules[path] = closure

    def get_module(self, path):
        """

        """
        return self.modules[path]
