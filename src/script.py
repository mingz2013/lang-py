# -*- coding:utf-8 -*-
"""
main
"""
__date__ = "14/12/2017"
__author__ = "zhaojm"

import os
import sys

from vm.env import ENV

sys.path.append(os.path.dirname("."))

from vm.vm import VM


def script(filename):
    """script"""
    env = ENV()

    env.compile_file(filename)

    print('=' * 100)

    vm = VM()
    vm.env = env
    vm.filename = filename

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
