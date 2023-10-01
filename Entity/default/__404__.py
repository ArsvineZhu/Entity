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


class Page404(Scene):
    """进入到了未知的页面
    Entered an unknown page"""

    def __init__(self):
        super().__init__("root/__404__")
        self.rect = None
        self.tip_2_3 = None
        self.tip_2_2 = None
        self.tip_2_1 = None
        self.tip_1_2 = None
        self.tip_1_1 = None
        self.error = None
        self.title = None
        self.u = Utility()

    def prepare(self, entity):
        self.u.entity = entity

        self.title = Text(
            "Oops! You seem to have entered an unknown world.",
            Utility.colors['white'],
            self.u.fsconvert(55, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(50), self.u.hpy(20)),
            entity,
            center=True
        )

        self.error = Text(
            "4 0 4",
            (30, 30, 30, 0),
            self.u.fsconvert(600, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(50), self.u.hpy(12)),
            entity,
            center=True
        )

        self.tip_1_1 = Text(
            "If you are an app user, then you may have encountered an internal error, please try restarting",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(40)),
            entity
        )

        self.tip_1_2 = Text(
            "and, if necessary, contact the app developer to resolve the issue.",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(45)),
            entity
        )

        self.tip_2_1 = Text(
            "If you are a developer, please check if the path exists when the page is switched",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(55)),
            entity
        )

        self.tip_2_2 = Text(
            "Don't get discouraged, take a break and work hard again!",
            Utility.colors['white'],
            self.u.fsconvert(24, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(60)),
            entity
        )

        self.tip_2_3 = Text(

            "Target Path: {pre}",
            Utility.colors['white'],
            self.u.fsconvert(20, entity.s.size, (16 * 65, 9 * 65)),
            (self.u.hpx(5), self.u.hpy(80)),
            entity
        )

        self.rect = Rect(Utility.colors['grey'], [0, 0, *entity.s.size], 0)

    def render(self, entity):
        self.rect.render(entity)
        self.error.render()
        self.title.render()
        self.tip_1_1.render()
        self.tip_1_2.render()
        self.tip_2_1.render()
        self.tip_2_2.render()
        self.tip_2_3.text = self.tip_2_3.text.replace('{pre}', entity.p.previous)
        self.tip_2_3.refresh()
        self.tip_2_3.render()
