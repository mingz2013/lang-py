# -*- coding:utf-8 -*-
"""
main
"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

import codecs
import os
import sys

sys.path.append(os.path.dirname("."))

from parser.parser import Parser
from prototype.prototype import ProtoType
from vm.vm import VM
from vm.closure import Closure

def script(filename):
    """script"""
    with codecs.open(filename, encoding='utf-8') as f:
        print('=' * 100)
        ast = Parser(filename, f.read()).parse_file()
        print('=' * 100)
        print('ast.execute result: >>', ast.execute())
        print('=' * 100)

        proto = ProtoType(None, filename)
        proto.name = filename

        ast.to_bin(proto)

        print("proto-->>", proto)
        print('=' * 100)

        vm = VM(filename)
        vm.proto = proto
        vm.init([])


def print_help():
    """print help"""
    print("script.py path")


def main():
    """main"""
    if len(sys.argv) != 2:
        print_help()
    else:

        filename = sys.argv[1]

        script(filename)


if __name__ == "__main__":
    main()
