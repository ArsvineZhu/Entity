# coding: utf-8
# python3.11
# entity - A simple module to aid in Pygame-based game development
# Copyright (C) 2023  Arsvine Zhu(朱一铭)
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Library General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# Made by Arsvine Zhu, in P.R.China
#
# Arsvine Zhu
# 2023/10/1

"""
Entity 是一组专为编写游戏而设计的 Python 模块。
它是在优秀的 Pygame 库之上编写的。
这允许您以一种更简单的方式在 Python 中创建功能齐全的游戏和多媒体程序语言。

Entity is a set of Python modules designed for writing games.
It is written on top of the excellent Pygame library. This allows you
to create fully functional games and multimedia programming languages
in Python in a simpler way.
"""

from Entity.strings import *
from Entity.default.default import default_pages
from Entity.settings import Settings
from Entity.crashhandler import CrashHandler
from Entity.render import Render
from Entity.utility import Utility
from Entity.path import Path
from Entity.events import *
import pygame
import os
from typing import Callable

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"


# import events, strings


class Entity:
    """Entity 是一组专为编写游戏而设计的 Python 模块。
    它是在优秀的 Pygame 库之上编写的。
    这允许您以一种更简单的方式在 Python 中创建功能齐全的游戏和多媒体程序语言。

    Entity is a set of Python modules designed for writing games.
    It is written on top of the excellent Pygame library. This allows you
    to create fully functional games and multimedia programming languages
    in Python in a simpler way.
    """

    def __init__(self) -> None:
        self.loop = None
        """循环方法
        Loop method"""

        self.active = False
        """窗口活动状态
        Window activity"""

        self.s = self.settings = Settings(self)
        """基本的屏幕设置
        Basic window setup information"""

        self.p = self.path = Path()
        """页面路径信息
        The page path information"""

        self.u = self.utility = Utility()
        """开发工具函数
        Utility functions"""

        self.r = self.render = Render(self)
        """渲染器
        Renderer"""

        self.c = self.crash_handler = CrashHandler()
        """异常崩溃处理
        Exception crash handling"""

        self.event_registered = {
            BUTTON_CLICK: []
        }
        """注册事件"""

    def register_event(self, listener: Callable):
        """注册一个事件"""
        # listener 是个页面元素, listener.event_type 是其事件类型
        # TODO 完善事件系统
        self.event_registered[listener.event_type].append(listener)

    def init(self) -> None:
        """初始化实体界面
        Initialize the entity interface"""

        print(PROCESS[self.s.lang]['Start'])
        self.settings.init()

        self.r.sm.register_all(default_pages)
        self.r.sm.load_all(default_pages)

        self.active = True

        print(PROCESS[self.s.lang]['Activate'])
        self.c.status.code(0, 'Basic')
        self.c.status.display()

    def run(self, loop: Callable) -> None:
        """启动窗口
        Start the window"""
        self.loop = loop
        self.c.status.code(1)
        print(PROCESS[self.s.lang]['Running'])

        while self.active:
            try:
                # 主循环体
                self._event_response()
                self.loop()
                # 填充主窗口的背景颜色
                self.s.screen.fill(self.s.color)
                self.r.render()

            except Exception as err:
                if self.active:
                    self.c.status.code(1, 'Error')
                    self.c.status.display(str(err))
            else:
                try:
                    pygame.display.update()  # 更新屏幕内容
                    self.s.FPS.tick(self.s.fps)  # 更新帧率

                except Exception as err:
                    if self.active:
                        self.c.status.code(1, 'Error')
                        self.c.status.display(str(err))

    def _event_response(self) -> None:
        """内部方法
        Internal method

        检查 PyGame 的事件
        Check PyGame's events"""
        # 循环获取事件，监听事件状态
        for event in pygame.event.get():

            # 判断用户是否点了"X"关闭按钮,并执行 if 代码段
            if event.type == pygame.QUIT:
                # 卸载所有模块
                pygame.quit()
                self.active = False
                # 终止程序，确保退出程序
                self.c.status.code(0, 'Exit')
                self.c.status.display()

            if event.type == pygame.VIDEORESIZE:
                # 窗口大小改变
                self.s.size = (event.size[0], event.size[0] / self.s.original_scale)
                self.s.screen = pygame.display.set_mode(self.s.size, pygame.RESIZABLE)

                # 卸载已加载的场景, 并重新计算布局
                self.r.sm.reload_all()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标按下
                for listener in self.event_registered[BUTTON_CLICK]:
                    # 处理按钮按下
                    if listener.__collide__.collidepoint(pygame.mouse.get_pos()):
                        listener.handle_event(BUTTON_CLICK)
