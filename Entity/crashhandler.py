#! python3.11

"""异常崩溃处理类
Exception crash handling class
"""

import sys

from Entity.strings import *


class CrashHandler:
    """异常崩溃处理类
    Exception crash handling class"""

    class Status:
        """状态信息类
        Status information class"""

        def __init__(self, code: int = -1):
            self.status = code
            """状态信息
            Status information"""
            self.t = self.types = ['Basic', 'Error', 'Exit']
            """所有信息类型
            All information types"""
            self._type = 'Basic'
            """信息类型
            Information type"""

            self.info = INFO_ZH
            """信息描述语句
            All information description statements"""

            self.stuck = STUCK_ZH
            """卡死
            stuck"""

            self.status_report = STATUS_REPORT['zh']

            self.str = str(self)
            """信息描述
            Description of the information"""

        def set_lang(self, lang: str = 'zh') -> None:
            """设置语言"""

            if lang == 'zh':
                self.info = INFO_ZH
                self.stuck = STUCK_ZH
                self.status_report = STATUS_REPORT['zh']
            elif lang == 'en':
                self.info = INFO_EN
                self.stuck = STUCK_EN
                self.status_report = STATUS_REPORT['en']
            else:
                raise Exception("未知语言 - Unknown language")

        def code(self, code: int, _type: str = 'Basic') -> None:
            """设置当前状态码
            Set the current status code"""

            self.status = code
            self._type = _type
            self.str = str(self)

        def display(self, err: str = '') -> None:
            """展示当前状态
            Display the current status"""

            print(str(self), self.info[self._type][self.status].replace(
                '{err}', ': ' + err), sep="\n-   ")

            if self._type == 'Error':
                print('\a')
                input(self.stuck)
                sys.exit()

        def __str__(self):
            return self.status_report[self._type] + str(self.status)

    def __init__(self) -> None:
        self.status = self.Status()
        """状态信息
        Status information"""
