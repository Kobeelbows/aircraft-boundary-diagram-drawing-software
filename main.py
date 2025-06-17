#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTranslator, QLocale
from widget import Widget

def main():
    # 创建应用程序
    app = QApplication(sys.argv)
    
    # 设置国际化支持
    translator = QTranslator()
    locale = QLocale.system().name()
    translator.load(f":/i18n/kobe_{locale}")
    app.installTranslator(translator)
    
    # 创建主窗口并显示
    window = Widget()
    window.show()
    
    # 执行应用程序事件循环
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 