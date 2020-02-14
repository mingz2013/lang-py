# -*- coding: utf-8 -*-
"""
@FileName: member
@Time: 2020/2/14 12:19
@Author: zhaojm

Module Description

"""


class Member(object):
    def __get_d(self):
        d = self.__dict__

        d['__class_name__'] = self.__class__.__name__

        return d

    def __str__(self):
        return str(self.__get_d())

    def __repr__(self):
        return repr(self.__get_d())

    def __init__(self):
        self.name = None
        self.data = None
        self.idx = None
