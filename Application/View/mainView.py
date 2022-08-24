# ！/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
# @Time         :   2022/8/22 10:21
# @Author       :   Dominance
# @File         :   mainView.py
# @Version      :   V 1.0.0
# @Description  :   主程序视图层
'''
from public import path
from Resource.ui.mainUI import mainUI
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui

class mainView(mainUI,QWidget):
    def __init__(self):
        super(mainView,self).__init__()
        self.Icon_path = path + '\\Resource\\static\\images\\Icon\\哆啦A梦.ico'
        self.setupUi(self)
        self.retranslateUi(self)
        self.ui_init()

    def ui_init(self):
        '''自定义UI'''
        # 设置窗口图标
        icon = QtGui.QIcon(self.Icon_path)
        self.setWindowIcon(icon)