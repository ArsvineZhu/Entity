#! python3.11
# main.py - 主程序

import sys

from TexasTheOmertosa import Texas
from Entity import entity
from stats import Stats


def main():
    """主程序"""
    s = Stats()
    size = s.size
    color = s.color

    e = entity.Entity()
    e.s.config(size, "Texas The Omertosa", color, 30, None)
    e.s.set_language('en')
    e.init()

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
