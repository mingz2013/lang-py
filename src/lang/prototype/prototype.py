# -*- coding: utf-8 -*-
"""

Module Description

"""
from typing import List

from lang import logger
from lang.instructions.instruction import Instruction
from lang.prototype.member import Member
from lang.prototype.var import Var


class ProtoType(object):

    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self, proto: 'ProtoType' = None, name: str = None):
        self.src: str = ""  # 源码，用于调试

        # bin code
        self.name: str = name  # 函数名, 或者文件名
        self.code: List[Instruction] = []  # 指令表
        self.constants: List[str | int | float] = []  # 常量表
        self.vars: List[Var] = []  # 变量 Var()
        # self.args = []  # 参数表

        self.members: List[Member] = []  # 成员，用于实现面向对象的属性名称 所有以this. 赋值的名称都存储到这里. 且这里的值可以被外部引用

        self.proto: ProtoType = proto  # 父级 ProtoType, 目前在 代码生成阶段使用到
        self.env = None  # env, 目前在代码生成阶段用到，用于存放全局module索引，编译多个文件

        self.protos: List[ProtoType] = []  # 子函数原型表

        self.for_scopes: List = []  # 用于生成代码阶段，记录for循环的作用域，用于处理break，continue

    def enter_for_scopes(self):
        self.for_scopes.append({
            'jmp_ends': [],
            'jmp_begins': []
        })

    def pop_for_scopes(self):
        return self.for_scopes.pop()

    def add_jmp_to_end_to_for_scopes(self, inst):
        self.for_scopes[-1]['jmp_ends'].append(inst)

    def add_jmp_to_begin_to_for_scopes(self, inst):
        self.for_scopes[-1]['jmp_begins'].append(inst)

    def add_name(self, n: str, local_must: bool = False):
        """

        :param n: 名称
        :param local_must: 是否一定要存储到本地
        """
        logger.debug('<<', n, local_must)

        if local_must:
            if self.find_name(n) >= 0:
                # local_must = True 的时候，肯定是第一次添加才对
                raise Exception('error in add name')
            var = Var()
            var.name = n
            var.data = None
            var.store_type = var.TYPE_STORE_LOCAL
            self.vars.append(var)
            return len(self.vars) - 1
        else:  # 不一定存储到本地
            # 如果本地没有，
            #   从上一级查找，直到找到所有的层级，
            #       如果有找到：
            #           就返回结果，并一层层存储下来，直到存储到本一层。
            #       如果没有找到：
            #           存储到本地
            i = self.find_super(n)
            if i < 0:
                # 上一级没找到，存储到本级
                var = Var()
                var.name = n
                var.data = None
                var.store_type = var.TYPE_STORE_LOCAL
                self.vars.append(var)
                i = len(self.vars) - 1
                var.idx = i

            return i

    def find_super(self, n: str) -> int:
        """
        从链上查找name
        """
        i = self.find_name(n)
        if i >= 0:
            # 本地找到直接返回
            return i

        if not self.proto:
            # 没有上一级直接返回
            return i

        i = self.proto.find_super(n)
        if i >= 0:
            # 上一级找到存储到本级
            v = Var()
            v.name = n
            v.store_type = v.TYPE_STORE_SUPER
            v.idx = i
            self.vars.append(v)
            return len(self.vars) - 1
        else:
            # 上一级也没找到返回
            return i

    def find_name(self, n: str) -> int:
        """
        从本级查找索引
        """
        for i, var in enumerate(self.vars):
            if var.name == n:
                return i
        return -1

    def get_name(self, idx: int) -> str:
        """
        用于调试打印，
        用于设置name store member
        """
        return self.vars[idx].name

    def add_member(self, n: str) -> int:
        """
        添加属性
        """
        idx = self.find_member(n)
        if idx >= 0:
            return idx
        member = Member()
        member.name = n
        self.members.append(member)
        idx = len(self.members) - 1
        member.idx = idx
        return idx

    def find_member(self, n: str) -> int:
        """
        查找属性
        """
        for i, member in enumerate(self.members):
            if member.name == n:
                return i
        return -1

    def add_constant(self, c: str | int | float) -> int:
        if c in self.constants:
            return self.constants.index(c)
        self.constants.append(c)
        return len(self.constants) - 1

    def load_constant(self, idx: int):
        return self.constants[idx]

    def add_sub_proto(self, p: "ProtoType") -> int:
        self.protos.append(p)
        return len(self.protos) - 1

    def load_sub_proto(self, idx: int) -> "ProtoType":
        return self.protos[idx]

    def add_code(self, code: Instruction) -> int:
        logger.debug("<<", code)
        self.code.append(code)
        return len(self.code) - 1

    def get_code(self, idx: int) -> Instruction:
        if idx >= len(self.code):
            return -1
        return self.code[idx]

    @property
    def code_len(self) -> int:
        return len(self.code)

    def clone(self):
        """
        clone
        """
        # 这里其实是应该创建一个闭包对象

    def parse(self, reader):
        """
        用于解析数据
        """

    def dump(self, writer):
        """
        用于写入文件
        """
