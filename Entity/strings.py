#! python3.11

"""
Entity 中使用的文本输出
"""

# For Crash Handler

INFO_ZH = {
    'Basic': {0: "运行正常"},
    'Error': {
        0: "未知错误",
        1: "发生了一个在主循环中的错误{err}",
        2: "要渲染的场景<{err}>尚未加载"
    },
    'Exit': {0: "正常退出"}
}

INFO_EN = {
    'Basic': {0: "Functioning normally"},
    'Error': {
        0: "Unknown error",
        1: "An error occurred in the main loop{err}",
        2: "The scene to be rendered <{err}> has not been loaded"
    },
    'Exit': {0: "Exit normally"}
}

STUCK_ZH = "发生卡顿, 程序已卡死..."
STUCK_EN = "The program process is stuck, enter to end the program..."

STATUS_REPORT = {
    'zh': {
        'Basic': '一般状态 状态码: ',
        'Error': '发生错误 状态码: ',
        'Exit': '程序退出 状态码: '
    },
    'en': {
        'Basic': 'Basic Status Code: ',
        'Error': 'Error Status Code: ',
        'Exit': 'Exit Status Code: '
    }
}

# For Render

RENDER = {
    'zh': {
        'Registering': '正在注册场景: <%s> ... \n',
        'Completed': '... 操作完成\n',
        'Exists': '场景 <%s> 已经注册过了',
        'Loading': '加载场景: <%s> ... \n',
        'Loaded': '场景 <%s> 已经加载过了',
        'Unloading': '卸载场景: <%s> ... \n',
        'Cannot unload': '你不可以卸载基本的页面 <%s>',
        'Not exist': '场景 <%s> 并不存在',
        'Not load': '将要渲染的场景 <%s> 还没有被加载'
    },
    'en': {
        'Registering': 'Registering scene: <%s> ... \n',
        'Completed': '... Completed\n',
        'Exists': 'Scene <%s> already exists',
        'Loading': 'Loading scene: <%s> ... \n',
        'Loaded': 'Scene <%s> has already been loaded',
        'Unloading': 'Unloading scene: <%s> ... \n',
        'Cannot unload': 'You cannot unload the basic page <%s>',
        'Not exist': 'Scene <%s> does not exist',
        'Not load': 'The scene to be rendered <%s> has not been loaded'
    }
}

# For Entity
PROCESS = {
    'zh': {
        'Start': '\n[S] 开始初始化窗口...\n',
        'Activate': '\n[A] 正在激活窗口...\n',
        'Running': '\n[R] 正在运行窗口...\n'
    },
    'en': {
        'Start': '\n[S] Starting initialization...\n',
        'Activate': '\n[A] Activating the window...\n',
        'Running': '\n[R] Running the window...\n'
    }
}

# For Settings
SETTINGS_STRINGS = {
    'zh': "[!] 默认字体未设定, 正在使用系统字体",
    'en': "[!] The default font is not set, and the system font is now used"
}

# For Elements
TIPS = {
    'zh': {},
    'en': {}
}
