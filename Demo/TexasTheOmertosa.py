#! python3.11

"""
Texas The Omertosa Page
Scene
"""

import Entity.scenes

from Entity import *
from stats import Stats

stats = Stats()
size = stats.size
assets = stats.assets_path


class Texas(Entity.scenes.Scene):
    """Texas 页面渲染"""

    def __init__(self):
        super().__init__("root/Texas")
        self.u = entity.Utility()

        # 设置附链
        self.support_adjunct = ["elite"]

        self.rect: elements.Rect | None = None

        self.bg_1: elements.Rect | None = None
        self.bg_2: elements.Rect | None = None

        self.fig_1: elements.Rect | None = None
        self.fig_2: elements.Rect | None = None

        self.charname: elements.Text | None = None
        self.charname_en: elements.Text | None = None

        self.charclass: elements.Image | None = None
        self.branch_bar: elements.SurfRect | None = None
        self.branch: elements.Image | None = None
        self.branch_text: elements.Text | None = None
        self.pos_bar: elements.SurfRect | None = None
        self.pos: elements.Text | None = None
        self.tags_bar: elements.SurfRect | None = None
        self.tags: elements.Text | None = None

        self.stars: elements.Rect | None = None

        self.buttons: dict[str, elements.Button | None] = {
            'elite_0': None,
            'elite_2': None
        }

        self.elite0_blue: elements.Rect | None = None
        self.elite2: elements.Rect | None = None
        self.elite0: elements.Rect | None = None
        self.elite2_blue: elements.Rect | None = None

        self.elite0_icon: elements.Rect | None = None
        self.elite2_icon: elements.Rect | None = None

    def prepare(self, e: entity.Entity):
        self.u.entity = e
        self.rect = elements.Rect(entity.Utility.colors['grey'], [0, 0, *e.s.size], 0)

        self.bg_1 = elements.Image(
            assets + "Bg_default.png",  # 1024 * 576
            x=0,
            y=0,
        )

        self.bg_2 = elements.Image(
            assets + "Bg_skin.png",  # 1024 * 576
            x=0,
            y=0,
        )

        self.fig_1 = elements.Image(
            assets + "Texas_1.webp",  # 2048 * 2048
            x=0,
            y=0,
            mode=2
        )

        self.fig_2 = elements.Image(
            assets + "Texas_2.webp",  # 2048 * 2048
            x=self.u.hpx(-24),
            y=self.u.hpy(-72.7),
            mode=2
        )

        self.fig_1.zoom(0.5)
        self.fig_2.zoom(1 / 1.35)

        self.charname = elements.Text(
            "缄默德克萨斯",
            (255, 255, 255),
            self.u.fsconvert(52, e.s.size, (1024, 576)),
            (self.u.hpx(1), self.u.hpy(78)),
            e,
            assets + "Charname.ttf"
        )

        self.charname_en = elements.Text(
            "Texas the Omertosa",
            (255, 255, 255),
            self.u.fsconvert(22, e.s.size, (1024, 576)),
            (self.u.hpx(1), self.u.hpy(74)),
            e,
            assets + "arialbd.ttf"
        )

        self.charclass = elements.Image(
            assets + "specialist.png",  # 2048 * 2048
            x=self.u.hpx(1),
            y=self.u.hpy(88),
            mode=2
        )
        self.charclass.zoom(0.2265)
        self.charclass.set_alpha(self.u.diaphaneity(30))

        self.branch_bar = elements.SurfRect((0, 0, 0, self.u.diaphaneity(30)),
                                            [self.u.hpx(7.5), self.u.hpy(88), self.u.hpx(10), self.u.hpy(4)])
        self.pos_bar = elements.SurfRect((0, 0, 0, self.u.diaphaneity(30)),
                                         [self.u.hpx(18.25), self.u.hpy(88), self.u.hpx(10), self.u.hpy(4)])
        self.tags_bar = elements.SurfRect((0, 0, 0, self.u.diaphaneity(30)),
                                          [self.u.hpx(7.5), self.u.hpy(93), self.u.hpx(20.75), self.u.hpy(5)])

        self.branch = elements.Image(
            assets + "executioner.png",  # 2048 * 2048
            x=self.u.hpx(9.5),
            y=self.u.hpy(88.5),
            mode=2
        )
        self.branch.zoom(0.35)
        self.branch.set_alpha(self.u.diaphaneity(30))

        self.branch_text = elements.Text(
            "处决者",
            (255, 255, 255),
            self.u.fsconvert(14, e.s.size, (1024, 576)),
            (self.u.hpx(12), self.u.hpy(88)),
            e,
            assets + "msyh.ttc"
        )

        self.pos = elements.Text(
            "近战位",
            (255, 255, 255),
            self.u.fsconvert(14, e.s.size, (1024, 576)),
            (self.u.hpx(21), self.u.hpy(88)),
            e,
            assets + "msyh.ttc"
        )

        self.tags = elements.Text(
            "快速复活  输出",
            (255, 255, 255),
            self.u.fsconvert(14, e.s.size, (1024, 576)),
            (self.u.hpx(13.25), self.u.hpy(93.5)),
            e,
            assets + "msyh.ttc"
        )

        self.stars = elements.Image(
            assets + "star_6.png",  # 2048 * 2048
            x=self.u.hpx(0.75),
            y=self.u.hpy(70),
            mode=2
        )
        self.stars.zoom(0.6)

        self.elite0_blue = elements.Image(
            assets + "elite0_blue.png",
            x=self.u.hpx(0.15),
            y=self.u.hpy(1),
            mode=2
        )
        self.elite0_blue.zoom(0.25)
        self.elite0_blue.set_alpha(self.u.diaphaneity(30))

        self.elite0 = elements.Image(
            assets + "elite0.png",
            x=self.u.hpx(0.15),
            y=self.u.hpy(1),
            mode=2
        )
        self.elite0.zoom(0.25)
        self.elite0.set_alpha(self.u.diaphaneity(30))

        elite_0 = elements.Text(
            "精英零",
            (0, 176, 255),
            self.u.fsconvert(22, e.s.size, (1024, 576)),
            (0, 0),
            e,
            assets + "Charname.ttf"
        )

        self.buttons['elite_0'] = elements.Button(
            elite_0,
            (0, 0, 0, e.u.diaphaneity(25)),
            (self.u.hpx(1.5), self.u.hpy(2), self.u.hpx(10), self.u.hpy(6.5)),
            status=True,
            cx=self.u.hpx(1.4), cy=self.u.hpy(1.1),
            bold=True,
            ocolor=(30, 30, 30), opx=0
        )

        self.elite0_icon = self.elite0_blue

        def btn_1(status: int):
            self.buttons['elite_0'].text.color = (0, 176, 255)
            self.buttons['elite_0'].opx = 0
            self.elite0_icon = self.elite0_blue

            e.p.adjunct['elite'] = '0'

            self.buttons['elite_2'].text.color = (255, 255, 255)
            self.buttons['elite_2'].opx = 0.8
            self.elite2_icon = self.elite2
            self.buttons['elite_2'].status = False

        self.buttons['elite_0'].set_response(btn_1)

        e.register_event(entity.BUTTON_CLICK, self.buttons['elite_0'])

        self.elite2 = elements.Image(
            assets + "elite2.png",
            x=self.u.hpx(12.3),
            y=self.u.hpy(-0.1),
            mode=2
        )
        self.elite2.zoom(0.25)
        self.elite2.set_alpha(self.u.diaphaneity(30))

        self.elite2_blue = elements.Image(
            assets + "elite2_blue.png",
            x=self.u.hpx(12.3),
            y=self.u.hpy(-0.1),
            mode=2
        )
        self.elite2_blue.zoom(0.25)
        self.elite2_blue.set_alpha(self.u.diaphaneity(30))

        elite_2 = elements.Text(
            "精英二",
            (255, 255, 255),
            self.u.fsconvert(22, e.s.size, (1024, 576)),
            (0, 0),
            e,
            assets + "Charname.ttf"
        )

        self.buttons['elite_2'] = elements.Button(
            elite_2,
            (0, 0, 0, e.u.diaphaneity(25)),
            (self.u.hpx(13.5), self.u.hpy(2), self.u.hpx(10), self.u.hpy(6.5)),
            cx=self.u.hpx(1.4), cy=self.u.hpy(1.1),
            bold=True,
            ocolor=(30, 30, 30), opx=1
        )

        self.elite2_icon = self.elite2

        def btn_2(status: int):
            self.buttons['elite_2'].text.color = (0, 176, 255)
            self.buttons['elite_2'].opx = 0
            self.elite2_icon = self.elite2_blue

            e.p.adjunct['elite'] = '2'

            self.buttons['elite_0'].text.color = (255, 255, 255)
            self.buttons['elite_0'].opx = 0
            self.elite0_icon = self.elite0
            self.buttons['elite_0'].status = False

        self.buttons['elite_2'].set_response(btn_2)
        e.register_event(entity.BUTTON_CLICK, self.buttons['elite_2'])

    def render(self, e: entity.Entity):
        self.rect.render(e)

        if e.p.adjunct['elite'] == '0':
            self.bg_1.render(e)
            self.fig_1.render(e)
        else:
            self.bg_2.render(e)
            self.fig_2.render(e)

        self.charname.render_bold(ocolor=(40, 40, 40), opx=1.2)
        self.charname_en.render_bold(ocolor=(40, 40, 40), opx=0.8)

        self.charclass.render(e)
        self.branch_bar.render(e)
        self.pos_bar.render(e)
        self.branch.render(e)
        self.branch_text.render()
        self.pos.render()
        self.tags_bar.render(e)
        self.tags.render()
        self.stars.render(e)

        for i in self.buttons.values():
            i.render(e)

        self.elite0_icon.render(e)
        self.elite2_icon.render(e)
