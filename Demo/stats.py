#! python3
# stats.py - 统计数据

"""
stats
统计数据
"""

# 资源文件目录访问
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from pygame import image


class Stats:
    """统计数据"""

    def __init__(self):
        """初始化数据"""

        # 窗口大小
        self.size = (1024, 576)
        self.zero = (0, 0)

        # 颜色
        self.color = (0, 0, 0)

        self.assets_path = os.path.dirname(__file__) + "$assets$".replace('$', os.path.sep)
        self.icon = image.load(self.assets_path + "favicon.ico")
        self.icon.set_colorkey((0, 0, 0))  # 黑色透明
