# ！/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
# @Time         :   2022/8/22 8:05
# @Author       :   Dominance
# @File         :   main.py
# @Version      :   V 1.0.0
# @Description  :   程序入口
'''
import sys
import public
from PyQt5.QtWidgets import QApplication
from Application.Controller.mainController import mainController
from PyQt5.Qt import QFont,Qt

if __name__ == '__main__':
    # 分辨率自适应
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # Qt从5.6.0开始，支持High-DPI
    app = QApplication(sys.argv)
    # 重置字体大小
    font = QFont("黑体")
    pointsize = font.pointSize()
    font.setPixelSize(pointsize)
    app.setFont(font)

    # 从控制层启动 主界面
    first_ui = mainController()

    sys.exit(app.exec_())