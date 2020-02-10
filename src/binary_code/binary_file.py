# -*- coding: utf-8 -*-
"""
@FileName: binary_file
@Time: 2020/2/7 15:14
@Author: zhaojm

Module Description

"""

from .prototype import ProtoType


class BinaryFile(object):
    def __init__(self, filename):
        self.filename = filename

        self.signature = None  # 签名 4 byte
        self.version = None  # 版本号 1 byte
        self.main_func = ProtoType()

        self.parse()

    def parse(self):
        """

        """
