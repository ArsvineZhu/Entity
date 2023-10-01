#! python3.11

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from pygame.surface import Surface
import pygame

from .strings import *


class Settings:
    """记录基本的屏幕设置信息
    Record basic window setup information"""

    def __init__(self, entity) -> None:
        self.entity = entity
        """自动传入的 Entity 实体
        The Entity is automatically passed in"""

        self.size: tuple[int, int] = (1080, 720)
        """窗口大小
        Window size"""

        self.title = "Utility Entity Default"
        """窗口标题
        Window title"""

        self.icon = None
        """窗口图标
        Window icon"""

        self.color = (0, 0, 0)
        """窗口背景色
        Window background color"""

        self.fps = 30
        """帧率
        FPS"""

        self.FPS = None
        """设置帧率限制
        Set the frame rate limit"""

        self.screen: Surface | None = None
        """Pygame 的主窗口
        The main window of Pygame"""

        self.fontdefault = None
        """默认字体, 设定后, 默认将使用系列内的字体渲染那些未传入字体的文本渲染
        Default font, when set, by default,
        will use font within it to render text that does not pass into the font"""

        self.lang = 'zh'

    def config(self,
               size: tuple,
               title: str,
               color: tuple,
               fps: int = 30,
               icon=None
               ):
        """设定窗口基本数据
        Set the basic data of the window"""

        self.size = size
        self.title = title
        self.icon = icon
        self.color = color
        self.fps = fps

    def set_language(self, lang: str = 'zh') -> None:
        """设定异常输出的语言
        Sets the language of the exception output"""

        if lang not in SETTINGS_STRINGS.keys():
            raise Exception("未知语言 - Unknown language")
        self.lang = lang
        self.entity.c.status.set_lang(lang)
        self.entity.r.set_lang(lang)

    def init(self):
        """初始化 pygame 模块及窗口
        Initialize the pygame module and window"""

        # 使用 pygame 之前必须初始化
        pygame.init()
        # 设置主屏窗口
        self.screen = pygame.display.set_mode(self.size)
        # 设置窗口的标题，即名称
        pygame.display.set_caption(self.title)
        # 设置帧率限制
        self.FPS = pygame.time.Clock()

        if not self.fontdefault:
            # 未设置默认字体
            print(SETTINGS_STRINGS[self.lang])
