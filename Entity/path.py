#! python3.11

"""页面路径信息类
    用于管理路径数据
    存储场景对应关系
    The page path information class
    Used to manage path data
    Store scene correspondence
"""

from typing import Dict


class Path:
    """页面路径信息类
    用于管理路径数据
    存储场景对应关系
    The page path information class
    Used to manage path data
    Store scene correspondence
    """

    def __init__(self) -> None:
        self.route = ["root.py"]
        """路径列表
        List of paths"""

        self.path = "root.py"
        """路径文本
        String of paths"""

        self.base = "root.py"
        """路径中主页面的名称
        The name of the master page in the path"""

        self.adjunct = {}
        """附链名称-信息对
        Adjunct_name-information pairs"""

        self.previous = "root.py"
        """上一个到达的路径
        The previous path arrived"""

    def _join(self) -> str:
        """内部使用
        返回路径短链文本
        Internal use
        Returns the path short text
        """

        return '/'.join(self.route)

    def format(self) -> str:
        """返回标准路径串
        Returns the standard path string"""

        ret = self._join()
        if self.adjunct:
            ret += '?' + \
                   ','.join([k + ':' + v for k, v in self.adjunct.items()])

        return ret

    def append(self, path: str) -> str:
        """添加页面
        Append a page

        参数 path 为路径信息
        """

        self.set_previous()

        self.route.append(path)
        self.path = path
        self.base = path
        self.adjunct = {}

        return self.path

    def reverse(self) -> str:
        """返回上一层页面
        Return to the previous page"""

        self.set_previous()

        if len(self.route) > 1:
            self.route.pop()
            self.path = self._join()
            self.base = self.route[-1]
            self.adjunct = {}
        return self.path

    def set_adjunct(self, key: str, value: str) -> Dict[str, str]:
        """附加或修改后缀信息
        Append or modify the adjunct information

        参数 key 为键
        参数 value 为值
        """

        self.adjunct[key] = value
        return self.adjunct

    def reverse_adjunct(self) -> None:
        """清除附加后缀
        Clean the adjuncts"""

        self.adjunct = {}

    @staticmethod
    def segment(path: str) -> tuple[list[str], dict[str, str]]:  # "root.py/operators/Texas?nav:open,bar:extended"
        """把分割路径为列表和附加字典
        Split the parameter path into list and adjunct dictionary"""

        route = path.split(
            "/")  # ["root.py", "operators", "Texas?nav:open,bar:extended"]
        end = route[-1].split("?")  # ["Texas", "nav:open,bar:extended"]
        route[-1] = end[0]  # "Texas"
        if len(end) > 1:
            # end[-1] -> "nav:open,bar:extended"
            adjunct = {i.split(":")[0]: i.split(":")[-1]
                       for i in end[-1].split(",")}
            return route, adjunct
        return route, {}

    def reach(self, path: str) -> tuple[list[str], dict[str, str]]:
        """传送至路径
        Move to the path"""

        self.set_previous()

        r = self.segment(path)
        self.route = r[0]
        self.path = self._join()
        self.base = r[0][-1]
        self.adjunct = r[1]
        return r

    def set_previous(self, pre: str = '') -> None:
        """设置上一个页面
        Set previous page"""
        if pre:
            self.previous = pre
        else:
            self.path = self._join()
            self.previous = self.path

    def __str__(self) -> str:
        return self.format()

    def __len__(self) -> int:
        return self.route.__len__()
