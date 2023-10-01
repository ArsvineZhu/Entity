#! python3.11

"""
部分默认的场景, 在 Entity 初始化后自动注册, 不可修改
Some default scenes. It is automatically registered after the Entity is initialized and cannot be modified
"""

from Entity.elements import *
from Entity.scenes import Scene
from Entity.utility import Utility

# 尝试查找默认中文字体
_fonts = ["Microsoft YaHei", "Microsoft JhengHei", "SimHei", "SimSun"]
_zh_font = ''
for f in _fonts:
    _zh_font = pygame.font.match_font(f)
    if _zh_font:
        break
del _fonts


class PageRoot(Scene):
    """根页面
    Root page"""

    def __init__(self):
        super().__init__("root")
        self.rect = None
        self.tip_2_4 = None
        self.tip_2_3 = None
        self.tip_2_2 = None
        self.tip_2_1 = None
        self.tip_1_2 = None
        self.tip_1_1 = None
        self.root = None
        self.title = None
        self.u = Utility()

    def prepare(self, entity):
        self.u.entity = entity

        self.title = Text(
            "Default Root Page",
            Utility.colors['white'],
            self.u.fsconvert(55, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(50), self.u.hpy(20)),
            entity,
            center=True
        )

        self.root = Text(
            "Root",
            (30, 30, 30, 0),
            self.u.fsconvert(600, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(50), self.u.hpy(12)),
            entity,
            center=True
        )

        if _zh_font:
            self.tip_1_1 = Text(
                "恭喜你已经成功进入了根页面, 也就是 Entity 模块最基本的演示界面. 欢迎来到这个崭新的世界!",
                Utility.colors['white'],
                self.u.fsconvert(20, entity.s.size, (16 * 65, 9 * 65)),
                (self.u.hpx(5), self.u.hpy(40)),
                entity,
                font=_zh_font
            )

            self.tip_1_2 = Text(
                "可是切莫高兴得太早, 因为这表明工作才刚刚开始, 加油工作吧! 在正式项目中不应该展示界面.",
                Utility.colors['white'],
                self.u.fsconvert(20, entity.s.size, (16 * 65, 9 * 65)),
                (self.u.hpx(5), self.u.hpy(45)),
                entity,
                font=_zh_font
            )

        self.tip_2_1 = Text(
            "Congratulations on successfully entering the root.py page, which is the most basic demo interface of",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(55)),
            entity
        )

        self.tip_2_2 = Text(
            "the Entity module. Welcome to this new world!",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(60)),
            entity
        )

        self.tip_2_3 = Text(
            "But don't rejoice too soon, because it shows that the work has just begun, come on!",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(65)),
            entity
        )

        self.tip_2_4 = Text(
            "This interface should not be shown in formal projects.",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(70)),
            entity
        )

        self.rect = Rect(Utility.colors['grey'], [0, 0, *entity.s.size], 0)

    def render(self, entity):
        self.rect.render(entity)
        self.root.render()
        self.title.render()
        self.tip_1_1.render()
        self.tip_1_2.render()
        self.tip_2_1.render()
        self.tip_2_2.render()
        self.tip_2_3.render()
        self.tip_2_4.render()
