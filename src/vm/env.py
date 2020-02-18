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
        self.modules = []  # path: closure
        self.protos = []

    def compile_file(self, filename):
        """

        """
        print("compile file...<<", filename)

        idx = self.find_proto(filename)
        if idx >= 0:
            return idx

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
            idx = self.add_proto(filename, proto)
            return idx

    def find_proto(self, filename):
        for idx, proto in enumerate(self.protos):
            if proto.name == filename:
                return idx
        return -1

    def add_proto(self, filename, proto):
        idx = self.find_proto(filename)
        if idx >= 0:
            self.protos[idx] = proto
        else:
            self.protos.append(proto)
            idx = len(self.protos) - 1
        return idx

    def get_proto(self, idx):
        return self.protos[idx]

    def set_module(self, closure):
        """

        """
        self.modules.append(closure)
        return len(self.modules) - 1

    def get_module(self, path):
        """

        """
        return self.modules[path]
