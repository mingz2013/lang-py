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

def script(filename):
    """script"""
    with codecs.open(filename, encoding='utf-8') as f:
        ast = Parser(filename, f.read()).parse_file()

        print('ast.execute result: >>', ast.execute())

        proto = ProtoType(filename)
        proto.name = filename

        ast.to_bin(proto)

        print("proto-->>", proto)

        vm = VM(filename)
        vm.prototype = proto
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
