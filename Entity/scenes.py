#! python3.11

"""
场景构建类
"""

from .path import Path


class Scene:
    """基本页面对象类, 属于 entity 模块
    应继承使用
    The basic page object class, which belongs to the entity module
    Should be inherited from use
    """

    class Meta:
        """附加设置信息
        Additional setup information
        """

        def __init__(self):
            # todo 完成附链类型检查

            self.ignore_surplus_adjunct = True
            """忽略多余附链
            Ignore surplus adjunct"""
            self.check_adjunct_type = False
            """强制去检查附链类型信息
            Force to check the adjunct type information"""
            self.adjunct_types = []
            """附链类型信息
            Adjunct type information"""

    def __init__(self, path: str = 'root.py') -> None:
        self.p = self.path = Path()
        """页面的路径信息
        Path information for the page"""

        self.p.reach(path)

        self.format = self.p.format()
        """格式化输出文本, 即自己的路径
        Format the output text, i.e. its own path"""

        self.support_adjunct = []
        """支持的附链
        Supported adjuncts"""

        self.meta = self.Meta()
        """附加设置信息
        Additional setup information"""

    def prepare(self, entity) -> str:
        """准备渲染所需的资源
        参数 entity 将自动传入
        Prepare the resources required for rendering
        The parameter entity is passed in automatically
        """

        return "Prepare of '%s'" % self.path

    def render(self, entity) -> str:
        """渲染此页面
        参数 entity 将自动传入
        Render this page
        The parameter entity is passed in automatically
        """

        return "Render of '%s'" % self.path

    def __str__(self) -> str:
        return self.format
