#! python3.11

import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame
from typing import Literal, Callable, Sequence

from .utility import Utility
# from .entity import Entity
from .events import *
# from .strings import *

# 文本描边用
_circle_cache = {}


class Text:
    """渲染文本
    Render text"""

    def __init__(self, text: str | bytes | None, color: tuple[int, int, int] | tuple[int, int, int, int], size: int,
                 pos: tuple[int | float, int | float],
                 entity,
                 font: str | bytes | None = None,
                 antialias: Literal[0, 1] | bool = True,
                 center: Literal[0, 1] | bool = False,
                 background: tuple[int, int, int] | tuple[int, int, int, int] | None = None
                 ) -> None:

        self.sur = None
        self.font_obj = None
        self.rect = None

        self.e = entity

        self.text = text
        self.color = color
        self.bg = background
        self.anti = antialias
        self.pos = pos
        self.f = font
        # print(f"[*] Setting font of '{self.text}': {self.f}")
        self.size = size
        self.center = center

        self.refresh()

    @staticmethod
    def _circlepoints(r: int | float) -> list:
        """计算描边"""
        r = int(round(r))
        if r in _circle_cache:
            return _circle_cache[r]
        x, y, e = r, 0, 1 - r
        _circle_cache[r] = points = []
        while x >= y:
            points.append((x, y))
            y += 1
            if e < 0:
                e += 2 * y - 1
            else:
                x -= 1
                e += 2 * (y - x) - 1
        points += [(y, x) for x, y in points if x > y]
        points += [(-x, y) for x, y in points if x]
        points += [(x, -y) for x, y in points if y]
        points.sort()
        return points

    def render_bold(self, ocolor=(0, 0, 0), opx=2):
        """渲染一个描边后的文本
        Render text after a stroke"""
        text = self.text
        font = self.font_obj
        gfcolor = self.color

        textsurface = font.render(text, True, gfcolor).convert_alpha()
        w = textsurface.get_width() + 2 * opx
        h = font.get_height()

        osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
        osurf.fill((0, 0, 0, 0))

        surf = osurf.copy()

        osurf.blit(font.render(text, True, ocolor).convert_alpha(), (0, 0))

        for dx, dy in self._circlepoints(opx):
            surf.blit(osurf, (dx + opx, dy + opx))

        surf.blit(textsurface, (opx, opx))

        self.sur = surf
        self.render()

    def render(self) -> None:
        """渲染文本至屏幕
        Render text to the screen"""
        # 将准备好的文本信息，绘制到主屏幕 Screen 上
        self.e.s.screen.blit(self.sur, self.rect)

    def refresh(self) -> None:
        """刷新文本对象
        Refresh the text object"""

        if not self.f and self.e.s.fontdefault:
            # 字体未传入, 而存在默认字体
            self.f = self.e.s.fontdefault
            # print(f"[!] Setting default font of '{self.text}': {self.f}")

        self.font_obj = pygame.font.Font(self.f, self.size)
        # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑
        # 第三个参数，RGB 模式的字体颜色；第四个参数，RGB 模式字体背景颜色
        self.sur = self.font_obj.render(self.text, self.anti, self.color, self.bg)

        self.rect = self.sur.get_rect()  # 获得显示对象的 rect 区域坐标
        if self.center:
            self.rect.center = self.pos  # 设置显示对象居中
        else:
            self.rect.x, self.rect.y = self.pos


class SurfRect:
    """绘制矩形, 由 Surface 实现
    Draw a rect, powered by Surface"""

    def __init__(self,
                 color: tuple[int, int, int, int] | Sequence[int],
                 rect: list[float | int, float | int, float | int, float | int],
                 ) -> None:
        self.color = color
        self.rect = rect
        self.surf = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        self.surf.fill(color)

    def render(self, entity) -> None:
        """渲染矩形至屏幕
        Render rect to the screen"""
        entity.s.screen.blit(self.surf, (self.rect[0], self.rect[1]))


class Rect:
    """绘制矩形
    Draw a rect"""

    def __init__(self,
                 color: tuple[int, int, int] | tuple[int, int, int, int] | Sequence[int],
                 rect: list[float | int, float | int, float | int, float | int],
                 width: int = 0 | Sequence[float],
                 border_radius: int = -1,
                 border_top_left_radius: int = -1,
                 border_top_right_radius: int = -1,
                 border_bottom_left_radius: int = -1,
                 border_bottom_right_radius: int = -1
                 ) -> None:
        self.color = color
        self.rect = rect
        self.width = width
        self.border_radius = border_radius
        self.border_top_left_radius = border_top_left_radius
        self.border_top_right_radius = border_top_right_radius
        self.border_bottom_left_radius = border_bottom_left_radius
        self.border_bottom_right_radius = border_bottom_right_radius

    def render(self, entity) -> None:
        """渲染矩形至屏幕
        Render rect to the screen"""
        pygame.draw.rect(
            entity.s.screen,
            self.color,
            self.rect,
            self.width,
            self.border_top_left_radius,
            self.border_top_right_radius,
            self.border_bottom_left_radius,
            self.border_bottom_right_radius
        )


class Image:
    """
    渲染一张图片
    参数 path 为文件路径
    参数 x, y 为坐标
    参数 mode 为图像处理模式, 默认 1, 0 为原图, 1 为 convert , 2 为 convert_alpha

    Render an image
    Parameter path is the file path
    Parameter x, y is the coordinate
    Parameter mode is the image processing mode,
    default 1, 0 is the original image, 1 is convert, 2 is convert_alpha
    """

    def __init__(self,
                 path: str | bytes,
                 x: int | float = 0,
                 y: int | float = 0,
                 mode: int = 1
                 ) -> None:
        self.path = path
        self.mode = mode
        self.x = x
        self.y = y

        # 预处理图片文件
        self.img = pygame.image.load(path)  # mode = 0 or other
        if self.mode == 1:
            self.img = self.img.convert()
        elif self.mode == 2:
            self.img = self.img.convert_alpha()

        self.size = self.img.get_size()

    def zoom(self, size: int | float) -> None:
        """缩放
        Zoom"""

        self.img = Utility.Transform.zoom(self.img, size)

    def rotate(self, angle: int | float) -> None:
        """旋转
        Rotate"""

        self.img = Utility.Transform.rotate(self.img, angle)

    def set_colorkey(self, color: tuple[int, int, int] | tuple[int, int, int, int]) -> None:
        """设定指定颜色透明
        Set the specified color alpha = 0"""

        self.img.set_colorkey(color)

    def set_alpha(self, alpha: int) -> None:
        """设定指定颜色透明
        Set the specified color alpha = 0"""

        self.img.set_alpha(alpha)

    def render(self, entity) -> None:
        """渲染图片至屏幕
        Render image to the screen"""
        entity.s.screen.blit(self.img, (self.x, self.y))


class Button:
    """按钮, 矩形使用 Surface"""

    def __init__(self,
                 text: Text,
                 color: tuple[int, int, int, int] | Sequence[int],
                 rect: tuple[float | int, float | int, float | int, float | int],
                 status: bool = False,
                 cx: float | int = 0, cy: float | int = 0,
                 bold: bool = False,
                 gfcolor=(255, 255, 255), ocolor=(0, 0, 0), opx=2
                 ) -> None:
        self.text = text  # Text 对象
        self.color = color
        self.rect = rect
        self.cx = cx
        self.cy = cy
        self.bold = bold
        self.gfcolor = gfcolor
        self.ocolor = ocolor
        self.opx = opx

        self.surf = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        self.surf.fill(color)

        # (x, y, l, w) -> (x + l / 2, y + w / 2)
        center = self.rect[2] / 2 + self.rect[0] + cx, self.rect[3] / 2 + self.rect[1] + cy
        self.text.center = True
        self.text.pos = center
        self.text.refresh()

        self.__collide__ = self.surf.get_rect()
        self.__collide__.topleft = (self.rect[0], self.rect[1])

        self.event_type = BUTTON_CLICK
        self.status = status
        self.response = None

    def render(self, entity) -> None:
        """渲染至屏幕
        Render to the screen"""
        entity.s.screen.blit(self.surf, (self.rect[0], self.rect[1]))
        if self.bold:
            self.text.render_bold(self.ocolor, self.opx)
        else:
            self.text.render()

    def set_response(self, func: Callable):
        """设置响应"""
        self.response = func

    def handle_event(self, event: int):
        """处理事件"""
        if event == BUTTON_CLICK:
            self.status = not self.status
        if self.response:
            self.response(self.status)
