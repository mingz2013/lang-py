# -*- coding: utf-8 -*-
"""

Module Description

"""


class Member(object):
    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self):
        self.name = None
        self.data = None
        self.idx = None
