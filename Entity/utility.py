#! python3.11

"""开发工具函数及方法类
Utility functions and method class for development
"""

import os
from math import pi

# from .entity import Entity

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
from pygame.surface import Surface
import pygame


class Utility:
    """开发工具函数及方法类
    Utility functions and method class for development"""

    colors = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'red': (255, 0, 0),
        'grey': (20, 20, 20)
    }

    def __init__(self, entity=None) -> None:
        self.entity = entity

    @staticmethod
    def get_center(x: int | float, y: int | float) -> tuple[float, float]:
        """返回 x, y 的中间位置坐标
        Returns the intermediate coordinates of x, y
        """

        return x / 2.0, y / 2.0

    # noinspection SpellCheckingInspection
    @staticmethod
    def fsconvert(size: int, screen: tuple[int, int], origin: tuple[int, int]) -> int:
        """仅限等比例窗口的字体大小换算, 返回换算后的字体大小
        Font size conversion for proportional windows only, return the converted font size
        """
        # 一定程度上平均非等比例的影响
        return int((screen[0] + screen[1]) / (origin[0] + origin[1]) * size)

    @staticmethod
    def hp(hp: int | float, ori: int) -> float:
        """百分比相对坐标
        Hundred percent relative coordinate"""
        return float((hp / 100.0) * ori)

    def hpx(self, hp: int | float) -> float:
        """百分比相对 x 坐标
        Hundred percent relative x position"""
        return float((hp / 100.0) * self.entity.s.size[0])

    def hpy(self, hp: int | float) -> float:
        """百分比相对 y 坐标
        Hundred percent relative y position"""
        return float((hp / 100.0) * self.entity.s.size[1])

    @staticmethod
    def diaphaneity(v: int | float) -> int:
        """百分比透明度换算至255不透明度"""
        return int(255 - (v / 100) * 255)

    @staticmethod
    def angle_to_radian(angle: int | float) -> float:
        """角度变换, 角度制到弧度制
        Angle transformation, angle to radian"""

        return float(angle * (pi / 180))

    @staticmethod
    def radian_to_angle(radian: int | float) -> float:
        """角度变换, 角度制到弧度制
        Angle transformation, radian to angle"""

        return float(radian * (180 / pi))

    class Transform:
        """图形变换
        Graphic transformations"""

        @staticmethod
        def scale(sur: Surface, size: tuple[int, int]) -> Surface:
            """大小缩放, 使用矩形大小
            Size scaling, using the rectangle size"""

            return pygame.transform.scale(sur, size)

        @staticmethod
        def scale_ratio(sur: Surface, ratio: int | float) -> Surface:
            """大小缩放, 使用比例数值
            Size scaling, using proportional value"""

            size = sur.get_size()
            return pygame.transform.scale(sur, (size[0] * ratio, size[1] * ratio))

        @staticmethod
        def rotate(sur: Surface, euler_angle: int | float) -> Surface:
            """顺时针旋转一定角度(角度制)
            Rotate an angle clockwise (angle system, not a radian system)"""

            return pygame.transform.rotozoom(sur, - float(euler_angle), 1.0)

        @staticmethod
        def zoom(sur: Surface, size: int | float) -> Surface:
            """缩放一定比例
            Zoom to some extent"""

            return pygame.transform.rotozoom(sur, 0, float(size))
