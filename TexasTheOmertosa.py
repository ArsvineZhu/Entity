#! python3.11

"""
Texas The Omertosa Page
Scene
"""

import Entity.scenes
from Entity import elements, entity
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
        # self.meta.adjunct_types = [int]
        # self.meta.ignore_surplus_adjunct = True
        # self.meta.check_adjunct_type = True

        self.author: elements.Text | None = None
        self.fps = 0
        self.FPS: elements.Text | None = None

        self.bg_1: elements.Image | None = None
        self.bg_2: elements.Image | None = None

        self.fig_1: elements.Image | None = None
        self.fig_2: elements.Image | None = None

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

        self.charlogo: elements.Image | None = None

        self.buttons: dict[str, elements.Button | None] = {
            'elite_0': None,
            'elite_2': None
        }

        self.elite0_blue: elements.Image | None = None
        self.elite2: elements.Image | None = None
        self.elite0: elements.Image | None = None
        self.elite2_blue: elements.Image | None = None
        self.elite0_text: elements.Text | None = None
        self.elite2_text: elements.Text | None = None

        self.elite0_icon: elements.Image | None = None
        self.elite2_icon: elements.Image | None = None

        self.painter_icon: elements.Image | None = None
        self.cv_icon: elements.Image | None = None
        self.painter: elements.Text | None = None
        self.cv: elements.Text | None = None
        self.plus_1: elements.Image | None = None
        self.plus_2: elements.Image | None = None
        self.info_bar_1: elements.SurfRect | None = None
        self.info_bar_2: elements.SurfRect | None = None

        # 立绘位置偏移量
        self.fig_cx = 0
        self.fig_cy = 0
        self.fig_cx_t = 0
        self.fig_cy_t = 0
        # 文本偏移量
        self.text_cx = 0

    def prepare(self, e: entity.Entity):
        self.u.entity = e

        # 立绘位置偏移量
        self.fig_cx = 0
        self.fig_cy = 0
        self.fig_cx_t = 0
        self.fig_cy_t = 0
        # 文本偏移量
        self.text_cx = 0

        self.text_cx = self.u.hpx(-25)  # 设置偏移量

        self.author = elements.Text(
            "Arsvine Zhu",
            (255, 255, 255),
            self.u.fsconvert(14, e.s.size, (1024, 576)),
            (self.u.hpx(90), self.u.hpy(2)),
            e,
            assets + "msyh.ttc"
        )

        self.FPS = elements.Text(
            "",
            (255, 255, 255),
            self.u.fsconvert(14, e.s.size, (1024, 576)),
            (self.u.hpx(95), self.u.hpy(95)),
            e,
            assets + "msyh.ttc"
        )

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

        self.bg_1.zoom(self.u.zoomrate(1))
        self.bg_2.zoom(self.u.zoomrate(1))

        self.fig_1 = elements.Image(
            assets + "Texas_1.webp",  # 2048 * 2048
            x=0,
            y=0,
            mode=2
        )

        self.fig_2 = elements.Image(
            assets + "Texas_2.webp",  # 2048 * 2048
            x=self.u.hpx(-24) + self.u.hpx(30),  # 动态偏移量补偿
            y=self.u.hpy(-72.7) + self.u.hpy(20),
            mode=2
        )

        self.fig_1.zoom(self.u.zoomrate(0.5))
        self.fig_2.zoom(self.u.zoomrate(1 / 1.35))

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
        self.charclass.zoom(self.u.zoomrate(0.2265))
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
        self.branch.zoom(self.u.zoomrate(0.35))
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
        self.stars.zoom(self.u.zoomrate(0.6))

        self.charlogo = elements.Image(
            assets + "Logo_Penguin_Logistics.png",  # 510 * 510
            x=self.u.hpx(1),
            y=self.u.hpy(5),
            mode=2
        )
        self.charlogo.set_color((100, 100, 100))
        self.charlogo.zoom(self.u.zoomrate(0.55))
        self.charlogo.set_alpha(self.u.diaphaneity(50))

        self.elite0_blue = elements.Image(
            assets + "elite0_blue.png",
            x=self.u.hpx(0.15),
            y=self.u.hpy(1),
            mode=2
        )
        self.elite0_blue.zoom(self.u.zoomrate(0.25))
        self.elite0_blue.set_alpha(self.u.diaphaneity(15))

        self.elite0 = elements.Image(
            assets + "elite0.png",
            x=self.u.hpx(0.15),
            y=self.u.hpy(1),
            mode=2
        )
        self.elite0.zoom(self.u.zoomrate(0.25))
        self.elite0.set_alpha(self.u.diaphaneity(15))

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

        self.elite0_text = elements.Text(
            "ELITE 0",
            (128, 128, 128),
            self.u.fsconvert(16, e.s.size, (1024, 576)),
            (self.u.hpx(5.5), self.u.hpy(1.5)),
            e,
            assets + "msyh.ttc"
        )

        def btn_1():
            self.buttons['elite_0'].text.color = (0, 176, 255)
            self.buttons['elite_0'].opx = 0
            self.elite0_icon = self.elite0_blue

            e.p.adjunct['elite'] = '0'
            self.fig_cx_t = 0
            self.fig_cy_t = 0

            self.buttons['elite_2'].text.color = (255, 255, 255)
            self.buttons['elite_2'].opx = 0.8
            self.elite2_icon = self.elite2
            self.buttons['elite_2'].status = False

        self.buttons['elite_0'].set_response(btn_1)

        e.register_event(self.buttons['elite_0'])

        self.elite2 = elements.Image(
            assets + "elite2.png",
            x=self.u.hpx(12.3),
            y=self.u.hpy(-0.1),
            mode=2
        )
        self.elite2.zoom(self.u.zoomrate(0.25))
        self.elite2.set_alpha(self.u.diaphaneity(15))

        self.elite2_blue = elements.Image(
            assets + "elite2_blue.png",
            x=self.u.hpx(12.3),
            y=self.u.hpy(-0.1),
            mode=2
        )
        self.elite2_blue.zoom(self.u.zoomrate(0.25))
        self.elite2_blue.set_alpha(self.u.diaphaneity(15))

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

        self.elite2_text = elements.Text(
            "ELITE 2",
            (128, 128, 128),
            self.u.fsconvert(16, e.s.size, (1024, 576)),
            (self.u.hpx(17.5), self.u.hpy(1.5)),
            e,
            assets + "msyh.ttc"
        )

        # self.elite2_text.

        def btn_2():
            self.buttons['elite_2'].text.color = (0, 176, 255)
            self.buttons['elite_2'].opx = 0
            self.elite2_icon = self.elite2_blue

            e.p.adjunct['elite'] = '2'
            self.fig_cx_t = self.u.hpx(-30)
            self.fig_cy_t = self.u.hpy(-20)

            self.buttons['elite_0'].text.color = (255, 255, 255)
            self.buttons['elite_0'].opx = 0
            self.elite0_icon = self.elite0
            self.buttons['elite_0'].status = False

        self.buttons['elite_2'].set_response(btn_2)
        e.register_event(self.buttons['elite_2'])

        self.info_bar_1 = elements.SurfRect((0, 0, 0, self.u.diaphaneity(30)),
                                            [self.u.hpx(1), self.u.hpy(55), self.u.hpx(24), self.u.hpy(5)])
        self.info_bar_2 = elements.SurfRect((0, 0, 0, self.u.diaphaneity(30)),
                                            [self.u.hpx(1), self.u.hpy(61), self.u.hpx(24), self.u.hpy(5)])
        self.painter_icon = elements.Image(
            assets + "painter.png",
            x=self.u.hpx(1.75),
            y=self.u.hpy(55.5),
            mode=2
        )
        self.painter_icon.zoom(self.u.zoomrate(0.9))
        self.painter_icon.set_alpha(self.u.diaphaneity(15))

        self.cv_icon = elements.Image(
            assets + "cv.png",
            x=self.u.hpx(1.75),
            y=self.u.hpy(61.75),
            mode=2
        )
        self.cv_icon.zoom(self.u.zoomrate(0.9))
        self.cv_icon.set_alpha(self.u.diaphaneity(15))

        self.painter = elements.Text(
            "幻象黑兔",
            (255, 255, 255),
            self.u.fsconvert(16, e.s.size, (1024, 576)),
            (self.u.hpx(10), self.u.hpy(55.5)),
            e,
            assets + "msyh.ttc"
        )

        self.cv = elements.Text(
            "田所梓",
            (255, 255, 255),
            self.u.fsconvert(16, e.s.size, (1024, 576)),
            (self.u.hpx(10.5), self.u.hpy(61.5)),
            e,
            assets + "msyh.ttc"
        )

        self.plus_1 = elements.Image(
            assets + "plus.png",
            x=self.u.hpx(22.5),
            y=self.u.hpy(56),
            mode=2
        )
        self.plus_1.zoom(self.u.zoomrate(0.5))
        self.plus_1.set_alpha(self.u.diaphaneity(15))

        self.plus_2 = elements.Image(
            assets + "plus.png",
            x=self.u.hpx(22.5),
            y=self.u.hpy(62),
            mode=2
        )
        self.plus_2.zoom(self.u.zoomrate(0.5))
        self.plus_2.set_alpha(self.u.diaphaneity(15))

    def render(self, e: entity.Entity):
        elements.BasicBackground.render(e)
        self.author.render()
        self.fps = e.s.FPS.get_fps()
        self.FPS.text = str(round(self.fps))
        self.FPS.refresh()

        # 偏移的进度
        cx_process = abs(self.fig_cx / self.u.hpx(-30))
        self.bg_1.set_alpha(self.u.diaphaneity(cx_process * 100))
        self.fig_1.set_alpha(self.u.diaphaneity(cx_process * 100))
        self.bg_2.set_alpha(self.u.diaphaneity(100 - cx_process * 100))
        self.fig_2.set_alpha(self.u.diaphaneity(100 - cx_process * 100))
        del cx_process

        self.bg_1.render(e)
        self.bg_2.render(e)
        self.FPS.render()

        self.charlogo.cx = self.fig_cx + self.text_cx
        self.charlogo.cy = self.text_cx
        self.charlogo.render(e)

        self.fig_1.cx = self.fig_cx - self.text_cx
        self.fig_1.cy = self.fig_cy
        self.fig_1.render(e)

        self.fig_2.cx = self.fig_cx - self.text_cx
        self.fig_2.cy = self.fig_cy
        self.fig_2.render(e)

        self.charname.set_offset(x=self.text_cx)
        self.charname.render_bold(ocolor=(40, 40, 40), opx=1.2)
        self.charname_en.set_offset(x=self.text_cx * 0.5)
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

        self.elite0_text.render()
        self.elite2_text.render()

        self.elite0_icon.render(e)
        self.elite2_icon.render(e)

        self.info_bar_1.render(e)
        self.info_bar_2.render(e)

        self.painter_icon.render(e)
        self.cv_icon.render(e)
        self.painter.render()
        self.cv.render()
        self.plus_1.render(e)
        self.plus_2.render(e)

        # 非线性迭代
        # 立绘
        self.fig_cx = self.u.Position.smooth(self.fig_cx, self.fig_cx_t, 0.2)
        self.fig_cy = self.u.Position.smooth(self.fig_cy, self.fig_cy_t, 0.1)
        # 文本
        self.text_cx = self.u.Position.smooth(self.text_cx, 0, 0.15)
