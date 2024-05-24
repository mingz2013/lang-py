"""
符号表管理
"""
from typing import Dict, List, Any

from lang import logger


class Var(object):
    """变量"""

    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self, name: str, scope_path: List[int], init_data: Any):
        self.scope_path: List[int] = scope_path  # 作用域路径
        self.name: str = name  # 变量名称
        self.init_data: Any = init_data  # 初值数据
        # self.inited = False  # 是否初始化
        # self.offset = 0  # 变量的栈帧偏移

        # def scopePathStr(self):
        #     """作用域路径"""
        #     ret = ""
        #     for p in self.scopePath:
        #         ret += "/%d" % p
        #     return ret

        # @classmethod
        # def create_with_token(cls, pos, tok, lit):
        #     """常量创建变量对象，只需要token里面的数据"""
        #     if tok == token.NUMBER:
        #         var = Var("<number>")  # 类型作为名字
        #         var.initData = int(lit)  # 值
        #         return var
        #     else:
        #         print("var error...")


class SymTab(object):
    """符号表管理"""

    def __str__(self):
        return f"{self.__class__.__name__}<{self.__dict__}>"

    def __repr__(self):
        return repr(self.__str__())

    def __init__(self):
        self.var_tab: Dict[str, List[Var]] = {}  # 变量表 {var_name: [Var()...]}
        self.cur_func = None  # 当前分析的函数
        self.scope_id: int = 0  # 当前作用域编号
        self.scope_path: List[int] = []  # 作用域路径 [0, 1, 2...]

    def enter(self) -> 'SymTab':
        """作用域管理，进入作用域"""
        logger.debug("enter...")
        self.scope_id += 1
        self.scope_path.append(self.scope_id)

        return self

    def leave(self) -> 'SymTab':
        """离开作用域"""
        logger.debug("<<")
        # , 回收变量
        path_len = len(self.scope_path)
        for name, vlist in self.var_tab.items():
            rmlist = []
            for v in vlist:
                l = len(v.scope_path)
                if l == path_len and v.scope_path[-1] == self.scope_path[-1]:
                    rmlist.append(v)
            for rmv in rmlist:
                vlist.remove(rmv)

        self.scope_path.pop()

        return self

    def add_var(self, name: str, init_data: Any) -> 'SymTab':
        """保存变量对象"""
        logger.debug("<<", name, init_data)

        var = Var(name, self.scope_path[:], init_data)

        if var.name not in self.var_tab:
            # 如果变量名称不在变量列表里，先创建对应的列表
            self.var_tab[var.name] = []

        if var.name[0] == '<':
            # 常量，直接添加进去
            # 添加进去
            self.var_tab[var.name].append(var)
        else:
            # 非常量，判断作用域，如果相同作用域内已存在，直接替换，如果不存在add进去
            vlist = self.var_tab[var.name]

            for v in vlist:
                if v.scope_path[-1] == var.scope_path[-1]:
                    # 存在同作用域同名变量，直接替换
                    vlist.remove(v)
                    break

            vlist.append(var)

        return self

    def get_var(self, name: str) -> Var:
        """获取变量对象"""
        logger.debug("<<", name)
        # 匹配name，匹配最长当前路径scopePath

        select = None

        if name in self.var_tab:
            vlist = self.var_tab[name]
            path_len = len(self.scope_path)
            max_len = 0
            for v in vlist:
                l = len(v.scope_path)
                # print("getvar...", v.scopePath, self.scopePath)
                if l <= path_len and v.scope_path[l - 1] == self.scope_path[l - 1]:
                    if l > max_len:
                        max_len = l
                        select = v

        if not select:
            logger.error("error...select...", name)
            exit(1)

        return select


if __name__ == "__main__":
    s = SymTab()
    logger.debug(s)
    s.add_var('a', 'a')
    logger.debug(s)
    s.add_var('b', 'b')
    logger.debug(s)
    s.enter()
    logger.debug(s)
    s.add_var('c', 'c')
    logger.debug(s)
    s.add_var('d', 'd')
    logger.debug(s)
    s.enter()
    logger.debug(s)
    s.add_var('e', 'e')
    logger.debug(s)
    s.add_var('f', 'f')
    logger.debug(s)
    s.leave()
    logger.debug(s)
    s.add_var('g', 'g')
    logger.debug(s)
    s.add_var('h', 'h')
    logger.debug(s)
