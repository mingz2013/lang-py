"""

token定义

"""

# 关键字
kw_or = "kw_or"  # or
kw_and = "kw_and"  # and
kw_not = "kw_not"  # not
kw_in = "kw_in"  # in
kw_is = "kw_is"  # is
kw_false = "kw_false"  # False
kw_true = "kw_true"  # True
kw_none = "kw_none"  # None

kw_print = "kw_print"  # print

kw_if = "kw_if"  # if
kw_elif = "kw_elif"  # elif
kw_else = "kw_else"  # else

kw_for = "kw_for"  # for
kw_continue = "kw_continue"  # continue
kw_break = "kw_break"  # break

kw_def = "kw_def"  # def
kw_return = "kw_return"  # return
kw_self = "kw_self"  # self

kw_import = "kw_import"  # import
kw_from = "kw_from"  # from
kw_as = "kw_as"  # as

# 标识符
tk_identifier = "tk_identifier"  # 标识符

# 字面值
tk_integer = "tk_integer"  # 整数字面值
tk_floatnumber = "tk_floatnumber"  # 小数字面值

tk_string = "tk_string"  # 字符串字面值

# 运算符
tk_plus = "tk_plus"  # +
tk_minus_sign = "tk_minus_sign"  # -
tk_star = "tk_star"  # *
tk_divide = "tk_divide"  # /
tk_remainder = "tk_remainder"  # %

tk_equal = "tk_equal"  # ==
tk_not_equal = "tk_not_equal"  # !=
tk_less_than = "tk_less_than"  # <
tk_less_than_or_equal = "tk_less_than_or_equal"  # <=
tk_greater_than = "tk_greater_than"  # >
tk_greater_than_or_equal = "tk_greater_than_or_equal"  # >=

# 分隔符
tk_assign = "tk_assign"  # "="
tk_period = "tk_period"  # "."
tk_left_parenthesis = "tk_left_parenthesis"  # "("
tk_right_parenthesis = "tk_right_parenthesis"  # ")"
tk_left_middle_bracket = "tk_left_middle_bracket"  # "["
tk_right_middle_bracket = "tk_right_middle_bracket"  # "]"
tk_left_braces = "tk_left_braces"  # {
tk_right_braces = "tk_right_braces"  # }
tk_semicolon = "tk_semicolon"  # ";"
tk_comma = "tk_comma"  # ","
tk_quotation_mark = "tk_quotation_mark"  # "'"
tk_double_quotation_mark = "tk_double_quotation_mark"  # "\""

tk_newline = "tk_newline"  # \n

ERROR = "ERROR"

EOF = "EOF"  # -1


class Token(object):
    """token"""

    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self, pos, tok, lit):
        self.tok: str = tok
        self.pos: int = pos
        self.lit: str = lit


class File(object):
    """文件"""

    def __init__(self, filename: str):
        self.filename: str = filename
