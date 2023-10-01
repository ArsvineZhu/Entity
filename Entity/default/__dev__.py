#! python3.11

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


class PageDev(Scene):
    """开发者页面
    Developer page"""

    def __init__(self):
        super().__init__("root/__dev__")
        self.rect = None
        self.tip_2_1 = None
        self.tip_1_1 = None
        self.root = None
        self.title = None
        self.u = Utility()

    def prepare(self, entity):
        self.u.entity = entity

        self.title = Text(
            "Developer Page",
            Utility.colors['white'],
            self.u.fsconvert(55, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(50), self.u.hpy(20)),
            entity,
            center=True
        )

        self.root = Text(
            "Developer",
            (30, 30, 30, 0),
            self.u.fsconvert(500, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(65), self.u.hpy(12)),
            entity,
            center=True
        )

        if _zh_font:
            self.tip_1_1 = Text(
                "这是开发者界面, 提供当前 Entity 既有数据的预览",  # TODO 提供当前 Entity 既有数据的预览
                Utility.colors['white'],
                self.u.fsconvert(20, entity.s.size, (16 * 65, 9 * 65)),
                (self.u.hpx(5), self.u.hpy(40)),
                entity,
                font=_zh_font
            )

        self.tip_2_1 = Text(
            "This is the developer interface that provides a preview of "
            "the existing data of the current Entity",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(55)),
            entity
        )

        self.rect = Rect(Utility.colors['grey'], [0, 0, *entity.s.size], 0)

    def render(self, entity):
        self.rect.render(entity)
        self.root.render()
        self.title.render()
        self.tip_1_1.render()
        self.tip_2_1.render()
