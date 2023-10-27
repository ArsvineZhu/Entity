#! python3.11
# main.py - 主程序

import sys

from Entity import entity
from TexasTheOmertosa import Texas
from stats import Stats


def main():
    """主程序"""
    s = Stats()
    size = s.size
    color = s.color
    icon = s.icon

    e = entity.Entity()

    e.s.config(size, "Texas The Omertosa", color,
               45, resizable=True, icon=icon)

    # e.s.set_language('en')
    e.init()
    e.s.screen

    e.r.sm.register(Texas)
    e.r.sm.load(Texas)

    def loop():
        pass

    # root/Texas?elite:0
    e.p.reach("root/Texas?elite:0")
    e.run(loop)


if __name__ == '__main__':
    main()
    sys.exit()
