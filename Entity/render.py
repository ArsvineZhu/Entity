#! python3.11

"""渲染器类
Renderer class
"""

import collections as col

from .scenes import Scene
from .default.default import default_paths
from .strings import *

LANGUAGE = RENDER['zh']


class Render:
    """渲染器类
    Renderer class"""

    def __init__(self, entity) -> None:
        self.entity = entity
        """自动传入的 Entity 实体
        The Entity is automatically passed in"""

        self.sm = self.SceneManager(self, default_paths)
        """场景管理系统
        Scene management system"""

        self.scenes = col.OrderedDict()  # 创建一个有序字典
        """场景路径-场景类对
        Scene_path-scene pairs"""

        self.loaded = {}
        """已加载的场景
        The loaded scenes"""

    class SceneManager:
        """场景管理系统"""

        def __init__(self, render, paths: list):
            self.r = render
            self.paths = paths

        def register(self, scene: type[Scene]) -> None:
            """注册一个场景
            Register a scene
            :type scene: object"""

            s = scene()
            print(LANGUAGE['Registering'] % str(s), end='')
            if str(s) in self.r.scenes.keys():
                raise Exception(LANGUAGE['Exists'] % str(s))
            else:
                self.r.scenes[str(s)] = scene
                print(LANGUAGE['Completed'])

        def register_all(self, scenes: list[type[Scene]]) -> None:
            """同时注册多个场景
            Register multiple scenes at the same time"""

            for scene in scenes:
                self.register(scene)

        def current_info(self) -> str:
            """输出对于当前渲染状态的描述性文本
            Output descriptive text for the current rendering state"""

            # todo 尚未做
            print('Scenes: ', self.r.scenes)
            print('Loaded scenes: ', self.r.loaded)
            return ''

        def load(self, scene: type[Scene]) -> None:
            """加载场景
            Load a scene"""

            s = scene()
            print(LANGUAGE['Loading'] % str(s), end='')
            if str(s) in self.r.loaded.keys():
                raise Exception(LANGUAGE['Loaded'] % str(s))
            else:
                self.r.loaded[str(s)] = s
                self.r.loaded[str(s)].prepare(self.r.entity)
                print(LANGUAGE['Completed'])

        def load_all(self, scenes: list[type[Scene]]) -> None:
            """同时加载多个场景
            Load multiple scenes at the same time"""

            for scene in scenes:
                self.load(scene)

        def unload(self, scene: type[Scene]) -> None:
            """卸载场景
            Unload a scene"""
            s = scene()
            print(LANGUAGE['Unloading'] % str(s), end='')
            if str(s) in self.r.loaded.keys():
                if str(s) in self.paths:
                    raise Exception(LANGUAGE['Cannot unload'] % str(s))
                else:
                    del self.r.loaded[str(s)]
                    print(LANGUAGE['Completed'])
            else:
                raise Exception(LANGUAGE['Not exist'] % str(s))

        def unload_all(self, scenes: list[type[Scene]]) -> None:
            """同时卸载多个场景
            Unload multiple scenes at the same time"""

            for scene in scenes:
                self.unload(scene)

    @staticmethod
    def set_lang(lang: str = 'zh') -> None:
        if lang not in RENDER.keys():
            raise Exception("未知语言 - Unknown language")
        global LANGUAGE
        LANGUAGE = RENDER[lang]

    def render(self) -> None:
        """渲染当前路径的页面
        Render the page of the current path"""

        path = self.entity.p.path  # 当前绝对路径, 不含附链
        if path in self.loaded.keys():  # 页面已加载
            self.loaded[path].render(self.entity)

        elif path in self.scenes.keys():  # 页面存在
            self.entity.c.status.code(2, 'Error')
            raise Exception(LANGUAGE['Not load'] % path)

        else:
            # 页面不存在, 进入未知页面
            self.entity.p.set_previous(self.entity.p.path)
            self.entity.p.reach("root/__404__")
