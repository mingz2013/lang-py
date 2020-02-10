# -*- coding:utf-8 -*-
"""

ast相关定义

"""
__date__ = "16/12/2017"
__author__ = "zhaojm"

from context import context
from instructions import instruction
from prototype.prototype import ProtoType
from token import token


class Node(object):
    """节点基类"""

    def __get_d(self):
        d = self.__dict__

        d['name'] = self.__class__.__name__

        return d

    def __str__(self):
        return str(self.__get_d())

    def __repr__(self):
        return repr(self.__get_d())

    def execute(self):
        """exe"""
        raise NotImplemented()

    def to_bin(self, proto):
        """
        to bin
        """
        print(self)
        raise NotImplemented()


class EndNode(Node):
    """终结符，叶子节点"""

    def __init__(self, pos, tok, lit):
        self.pos = pos
        self.tok = tok
        self.lit = lit

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "tok": self.tok,
    #         "pos": self.pos,
    #         "lit": self.lit
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "tok": self.tok,
    #         "pos": self.pos,
    #         "lit": self.lit
    #     })


class StringLiteral(EndNode):
    """字符串字面值"""

    def execute(self):
        """exe"""
        return self.lit[1:-1]  # 去掉双引号

    def to_bin(self, proto):
        idx = proto.add_constant(self.lit[1:-1])

        inst = instruction.LoadConst(idx)

        proto.add_code(inst)


class DigitLiteral(EndNode):
    """数字字面值"""


class Integer(DigitLiteral):
    """整数字面值"""

    def execute(self):
        """exe"""
        return int(self.lit)

    def to_bin(self, proto):
        idx = proto.add_constant(int(self.lit))
        inst = instruction.LoadConst(idx)

        proto.add_code(inst)


class FloatNumber(DigitLiteral):
    """小数字面值"""

    def execute(self):
        """exe"""
        return float(self.lit)

    def to_bin(self, proto):
        idx = proto.add_constant(float(self.lit))
        inst = instruction.LoadConst(idx)

        proto.add_code(inst)


class Identifier(EndNode):
    """标识符"""

    def execute(self):
        """execute"""
        # return self.expression.execute()
        # 从环境变量，符号表管理里面，获取当前标识符所对应的值
        return context.Symtab.get_var(self.lit).init_data

    def to_bin(self, proto):
        idx = proto.add_name(self.lit)

        inst = instruction.LoadName(idx)

        proto.add_code(inst)


class Atom(Node):
    """原子"""


class ExpressionList(Atom):
    """表达式列表"""

    def __init__(self):
        self.expression_list = []

    def __len__(self):
        return len(self.expression_list)

    def append_expression(self, expression):
        """execute"""
        self.expression_list.append(expression)

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "expression_list": self.expression_list
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "expression_list": self.expression_list
    #     })

    def execute(self):
        """execute"""
        return [expression.execute() for expression in self.expression_list]

    def to_bin(self, proto):
        return [expression.to_bin(proto) for expression in self.expression_list]


class ListDisplay(Atom):
    """列表显示"""

    def __init__(self, expression_list):
        self.expression_list = expression_list

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "expression_list": self.expression_list
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "expression_list": self.expression_list
    #     })

    def execute(self):
        """exe"""
        return self.expression_list.execute()

    def to_bin(self, proto):
        """

        """
        self.expression_list.to_bin(proto)

        length = len(self.expression_list)

        inst = instruction.MakeList(length)

        proto.add_code(inst)


class ParenthForm(Atom):
    """
    圆括号形式
    """

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return str({
            "name": self.__class__.__name__,
            "expression": self.expression
        })

    def __repr__(self):
        return repr({
            "name": self.__class__.__name__,
            "expression": self.expression
        })

    def execute(self):
        """exe"""
        return self.expression.execute()

    def to_bin(self, proto):
        return self.expression.to_bin(proto)


class Call(Atom):
    """调用"""

    def __init__(self, identifier, expression_list):
        self.identifier = identifier
        self.expression_list = expression_list

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "identifier": self.identifier,
    #         "expression_list": self.expression_list
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "identifier": self.identifier,
    #         "expression_list": self.expression_list
    #     })

    def execute(self):
        """exe"""
        func = self.identifier.execute()

        return func(self.expression_list.execute())

    def to_bin(self, proto):
        self.identifier.to_bin(proto)

        for e in self.expression_list:
            e.to_bin(proto)

        inst = instruction.CallFunction(len(self.expression_list))
        proto.add_code(inst)


class Expression(Node):
    """表达式"""


class UnaryExpression(Expression):
    """一元运算符"""

    def __init__(self, tok, expression):
        self.tok = tok
        self.expression = expression

    def execute(self):
        """exe"""
        if self.tok == token.tk_plus:
            return self.expression.execute()
        elif self.tok == token.tk_minus_sign:
            return -self.expression.execute()
        else:
            print('UnaryExpression >> error tok', self.tok)
            return None

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "tok": self.tok,
    #         "expression": self.expression
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "tok": self.tok,
    #         "expression": self.expression
    #     })

    def to_bin(self, proto):
        """

        """
        self.expression.to_bin(proto)

        inst = instruction.Push(0)
        proto.add_code(inst)
        if self.tok == token.tk_plus:
            proto.add_code(instruction.Add())
        elif self.tok == token.tk_minus_sign:
            proto.add_code(instruction.Sub())


class NegativeExpression(UnaryExpression):
    """负数"""


class PositiveExpression(UnaryExpression):
    """正数"""


class BinaryOperationExpression(Expression):
    """二元运算符"""

    def __init__(self, left, right):
        self.left = left
        self.right = right

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "left": self.left,
    #         "right": self.right
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "left": self.left,
    #         "right": self.right
    #     })

    def execute(self):
        """exe"""
        raise NotImplemented()


class RelationalExpression(BinaryOperationExpression):
    """加减类运算表达式"""


class MultiplicativeExpression(BinaryOperationExpression):
    """乘除类运算表达式"""


class PlusExpression(BinaryOperationExpression):
    """add"""

    def execute(self):
        """exe"""
        return self.left.execute() + self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)

        proto.add_code(instruction.Add())


class MinusSignExpression(RelationalExpression):
    """sub"""

    def execute(self):
        """exe"""
        return self.left.execute() - self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Sub())


class StarExpression(RelationalExpression):
    """mul"""

    def execute(self):
        """exe"""
        return self.left.execute() * self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Mul())


class DivideExpression(MultiplicativeExpression):
    """div"""

    def execute(self):
        """exe"""
        return self.left.execute() / self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Div())


class RemainderExpression(BinaryOperationExpression):
    """求余"""

    def execute(self):
        """exe"""
        return self.left.execute() % self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Rem())


class ComparisonExpression(BinaryOperationExpression):
    """比较运算表达式"""


class EqualExpression(ComparisonExpression):
    """等于"""

    def execute(self):
        """exe"""
        return self.left.execute() == self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Eq())


class NotEqualExpression(ComparisonExpression):
    """不等于"""

    def execute(self):
        """exe"""
        return self.left.execute() != self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Neq())


class LessThanExpression(ComparisonExpression):
    """小于"""

    def execute(self):
        """exe"""
        return self.left.execute() < self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Lt())


class LessThanOrEqualExpression(ComparisonExpression):
    """小于等于"""

    def execute(self):
        """exe"""
        return self.left.execute() <= self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Lte())


class GreaterThanExpression(ComparisonExpression):
    """大于"""

    def execute(self):
        """exe"""
        return self.left.execute() > self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Gt())


class GreaterThanOrEqualExpression(ComparisonExpression):
    """大于等于"""

    def execute(self):
        """exe"""
        return self.left.execute() >= self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Gte())


class IsExpression(ComparisonExpression):
    """is表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() is self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Is())


class InExpression(ComparisonExpression):
    """in表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() in self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.In())


class BooleanExpression(BinaryOperationExpression):
    """布尔运算表达式"""


class OrExpression(BooleanExpression):
    """or运算表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() or self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.Or())


class AndExpression(BooleanExpression):
    """and运算表达式"""

    def execute(self):
        """exe"""
        return self.left.execute() and self.right.execute()

    def to_bin(self, proto):
        """"""
        self.left.to_bin(proto)
        self.right.to_bin(proto)
        proto.add_code(instruction.And())


class NotExpression(Expression):
    """not运算表达式"""

    def __init__(self, expression):
        self.expression = expression

    def execute(self):
        """exe"""
        return not self.expression.execute()

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "expression": self.expression
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "expression": self.expression
    #     })

    def to_bin(self, proto):
        """"""
        self.expression.to_bin(proto)
        proto.add_code(instruction.Not())


class Statement(Node):
    """语句"""


class SimpleStatement(Statement):
    """简单语句"""

    def __init__(self):
        self.small_statements = []

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "small_statements": self.small_statements
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "small_statements": self.small_statements
    #     })

    def append_small_statement(self, node):
        """
        append_small_statement
        :param node:
        :return:
        """
        self.small_statements.append(node)

    def execute(self):
        """exe"""
        result = None
        for statement in self.small_statements:
            result = statement.execute()

        return result

    def to_bin(self, proto):
        for s in self.small_statements:
            s.to_bin(proto)


class SmallStatement(Statement):
    """SmallStatement"""


class PrintStatement(SimpleStatement):
    """print"""

    def __init__(self, expression_list):
        self.expression_list = expression_list

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "expression_list": self.expression_list
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "expression_list": self.expression_list
    #     })

    def execute(self):
        """exe"""
        print("PrintStatement.execute print >>>", self.expression_list.execute())
        return None

    def to_bin(self, proto):
        self.expression_list.to_bin(proto)
        proto.add_code(instruction.Print(len(self.expression_list)))


class AssignmentStatement(SimpleStatement):
    """赋值语句"""

    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "identifier": self.identifier,
    #         "expression": self.expression
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "identifier": self.identifier,
    #         "expression": self.expression
    #     })

    def execute(self):
        """execute"""
        context.Symtab.add_var(self.identifier.lit, self.expression.execute())
        return None

    def to_bin(self, proto):
        """

        """
        idx = self.identifier.to_bin(proto)
        self.expression.to_bin(proto)
        proto.add_code(instruction.StoreName(idx))


class ExpressionStatement(SimpleStatement):
    """表达式语句"""


class CompoundStatement(Statement):
    """复合语句"""


class DefStatement(Statement):
    """
    定义语句，函数定义
    """

    def __init__(self, identifier, expression_list, block):
        self.identifier = identifier
        self.expression_list = expression_list
        self.block = block

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'identifier': self.identifier,
    #         'expression_list': self.expression_list,
    #         'block': self.block
    #     })
    #
    # def __repr__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'identifier': self.identifier,
    #         'expression_list': self.expression_list,
    #         'block': self.block
    #     })

    def execute(self):
        """
        exe
        """
        # context.Symtab.add_var(self.ident.lit, )
        return None

    def to_bin(self, proto):
        p = ProtoType()
        p.name = self.identifier.lit
        p.args = self.expression_list

        self.block.to_bin(p)

        proto.add_sub_proto(p)

        proto.add_constant(p.name)
        proto.add_code('store const')
        proto.add_code("make function")


class ParamList(Node):
    """
    参数列表
    """

    def __init__(self):
        self.params = []

    def append_identifier(self, ident):
        self.params.append(ident)

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'params': self.params
    #     })
    #
    # def __repr__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'params': self.params
    #     })

    def execute(self):
        """"""

    def to_bin(self, proto):
        """"""


class StatementBlock(Node):
    def __init__(self):
        self.statements = []

    def append_statement(self, node):
        self.statements.append(node)

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'statements': self.statements,
    #     })
    #
    # def __repr__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'statements': self.statements,
    #     })

    def execute(self):
        ret = None
        for s in self.statements:
            ret = s.execute()
        return ret

    def to_bin(self, proto):
        for s in self.statements:
            s.to_bin(proto)


class ForStatement(Statement):
    """
    for 循环语句
    """

    def __init__(self, expression, block):
        self.expression = expression
        self.block = block

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'expression': self.expression,
    #         'block': self.block
    #     })
    #
    # def __repr__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'expression': self.expression,
    #         'block': self.block
    #     })

    def execute(self):
        ret = None
        while self.expression.execute():
            ret = self.block.execute()
        return ret

    def to_bin(self, proto):
        """"""


class IfStatement(Statement):
    """
    if 分支语句
    """

    def __init__(self):
        self.elifs = []

        self.else_block = None

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'elifs': self.elifs,
    #         'else_block': self.else_block
    #     })
    #
    # def __repr__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         'elifs': self.elifs,
    #         'else_block': self.else_block
    #     })

    def append_elif(self, expression, block):
        self.elifs.append({
            'expression': expression,
            'block': block
        })

    def set_else_block(self, else_block):
        self.else_block = else_block

    def execute(self):
        for elif_obj in self.elifs:
            if elif_obj['expression'].execute():
                return elif_obj['block'].execute()
        return self.else_block.execute()

    def to_bin(self, proto):
        """"""


class File(Node):
    """root"""

    def __init__(self):
        self.statements = []  # 语句集合

    # def __str__(self):
    #     return str({
    #         "name": self.__class__.__name__,
    #         "statements": self.statements
    #     })
    #
    # def __repr__(self):
    #     return repr({
    #         "name": self.__class__.__name__,
    #         "statements": self.statements
    #     })

    def append_statements(self, statement):
        """append statements"""
        self.statements.append(statement)

    def execute(self):
        """execute"""
        context.Symtab.enter()  # 进入0级作用域
        result = None
        for statement in self.statements:
            result = statement.execute()

        context.Symtab.leave()  # 离开0级作用域

        return result

    def to_bin(self, proto):
        for s in self.statements:
            s.to_bin(proto)


if __name__ == '__main__':
    f = File()
    # print(str(f.__dict__))
    print(f)
