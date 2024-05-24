# -*- coding: utf-8 -*-
"""

Module Description

"""

import codecs
from typing import List

from lang import logger
from lang.parser.parser import Parser
from lang.prototype.prototype import ProtoType
from lang.vm.closure import Closure


class ENV(object):
    def __init__(self):
        self.modules: List[Closure] = []  # path: closure
        self.protos: List[ProtoType] = []

    def compile_file(self, filename: str) -> int:
        """

        """
        logger.debug("<<", filename)

        idx = self.find_proto(filename)
        if idx >= 0:
            return idx

        with codecs.open(filename, encoding='utf-8') as f:
            logger.debug('=' * 100)

            ast = Parser(filename, f.read()).parse_file()

            logger.debug('=' * 100)

            # print('ast.execute result: >>', ast.execute())

            logger.debug('=' * 100)

            proto = ProtoType(None, filename)
            proto.name = filename
            proto.env = self

            ast.to_bin(proto)

            logger.debug("proto-->>", proto)
            idx = self.add_proto(filename, proto)
            return idx

    def find_proto(self, filename: str) -> int:
        for idx, proto in enumerate(self.protos):
            if proto.name == filename:
                return idx
        return -1

    def add_proto(self, filename: str, proto: ProtoType) -> int:
        idx = self.find_proto(filename)
        if idx >= 0:
            self.protos[idx] = proto
        else:
            self.protos.append(proto)
            idx = len(self.protos) - 1
        return idx

    def get_proto(self, idx: int) -> ProtoType:
        return self.protos[idx]

    def set_module(self, closure: Closure) -> int:
        """

        """
        self.modules.append(closure)
        return len(self.modules) - 1

    def get_module(self, path: int) -> Closure:
        """

        """
        return self.modules[path]
