# ！/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
# @Time         :   2022/8/22 10:20
# @Author       :   Dominance
# @File         :   mainController.py
# @Version      :   V 1.0.0
# @Description  :   主程序控装层
'''
import os
import time
import public
from Application.View.mainView import mainView
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QMessageBox,QFileDialog
from Common.operation import *

class mainController:
    def __init__(self):
        '''主界面控制层 类 初始化'''
        # 配置文件路径
        # self.ini = public.path + '\\Resource\\static\\config\\config.ini'
        # self.ini = public.path + '\\config.ini'
        self.ini = 'C:\\Offine_tools_config\\config.ini'
        # print(self.ini)
        # 创建界面对象
        self.mainView = mainView()
        # 槽函数 信号 初始化
        self.event_init()
        # 加载配置
        self.load_setting()
        # 初始化
        self.init()
        # 实例化显示
        self.mainView.show()

    # 槽函数 信号 初始化
    def event_init(self):
        '''槽函数 信号 初始化'''
        # 一键断联
        self.mainView.StartButton.clicked.connect(self.Start)
        # 断网按钮
        self.mainView.BreakButton.clicked.connect(self.Break)
        # 联网按钮
        self.mainView.LinkButton.clicked.connect(self.Link)
        # 程序生成
        self.mainView.GenerateButton.clicked.connect(self.Generate)
        # 保存配置
        self.mainView.SaveButton.clicked.connect(self.save_setting)
        # 选择路径
        self.mainView.ChooseButton.clicked.connect(self.load_path)
        # 重写关闭窗口事件
        self.mainView.closeEvent = self.close_event

    # 初始化
    def init(self):
        # 删除规则
        delete()

    def write_instructions_file(self):
        try:
            file = open('C:\\Offine_tools_config\\文件说明.txt', 'w')
            file.write('此目录为 Offine tools 工具的配置文件目录')
        except Exception as e:
            print(e)

    # 重写关闭窗口事件
    def close_event(self,event):
        # 删除规则
        delete()
        # 在配置文件夹这种写入说明文件
        self.write_instructions_file()
        event.accept()

    # 保存界面配置
    def save_setting(self):
        def show_msg():
            QMessageBox.information(self.mainView,'温馨提示', '配置保存成功')
        '''保存界面配置'''
        settings = QSettings(self.ini, QSettings.IniFormat)
        # 设置 格式
        settings.setIniCodec('utf8')
        # 获取参数
        path = self.mainView.lineEdit_path.text()
        delay_time = self.mainView.lineEdit_time.text()
        # 配置 字典
        setting_dict = {
            'path':path,
            'delay_time':delay_time,
        }
        # 循环遍历 保存配置
        for key, val in setting_dict.items():
            settings.setValue(key, val)

        # 弹窗提示
        show_msg()

    def load_setting(self):
        '''加载配置'''
        # 判断文件路径是否存在
        if os.path.exists(self.ini):
            # 获取配置文件 配置内容
            settings = QSettings(self.ini,QSettings.IniFormat)
            # 设置 格式
            settings.setIniCodec('utf8')
            # 读取配置
            path = settings.value('path')
            delay_time = settings.value('delay_time')
            # 界面显示
            self.mainView.lineEdit_path.setText(path)
            self.mainView.lineEdit_time.setText(delay_time)

    def load_path(self):
        '''选择并加载文件'''
        file_path, file_type = QFileDialog.getOpenFileName(self.mainView,'请选择程序路径','E:/','All Files (*);;EXE Files (*.exe)')
        if file_path:
            if '.exe' in file_path:
                self.mainView.lineEdit_path.setText(file_path)


    def Start(self):
        def show_msg():
            QMessageBox.warning(self.mainView, '警告', '延时时间错误')
        def show_msg_2():
            QMessageBox.warning(self.mainView, '警告', '延时时间不能为负数')
        def show_msg_3():
            QMessageBox.warning(self.mainView, '警告', '请先进行程序生成')
        # 截图读数-数字检测
        def Is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                pass
            try:
                import unicodedata
                unicodedata.numeric(s)
                return True
            except (TypeError, ValueError):
                pass
            return False
        if public.Generate_Sign == True:
            if Is_number(self.mainView.lineEdit_time.text()) == True:
                if int(self.mainView.lineEdit_time.text()) >= 0:
                    off()
                    time.sleep(int(self.mainView.lineEdit_time.text()))
                    reconnection()
                else:
                    show_msg_2()
            else:
                show_msg()
        else:
            show_msg_3()


    def Break(self):
        def show_msg():
            QMessageBox.warning(self.mainView, '警告', '请先进行程序生成')
        if public.Generate_Sign == True:
            off()
        else:
            show_msg()

    def Link(self):
        def show_msg():
            QMessageBox.warning(self.mainView, '警告', '请先进行程序生成')
        if public.Generate_Sign == True:
            reconnection()
        else:
            show_msg()


    def Generate(self):
        def show_msg():
            QMessageBox.information(self.mainView,'温馨提示', '程序生成完成')
        def show_msg_2():
            QMessageBox.warning(self.mainView, '警告', '程序路径错误')
        def show_msg_3():
            QMessageBox.warning(self.mainView, '警告', '程序已生成，无需再次生成')
        if public.Generate_Sign == False:
            if '.exe' in self.mainView.lineEdit_path.text():
                add(self.mainView.lineEdit_path.text().replace('/', '\\'))
                public.Generate_Sign = True
                show_msg()
            else:
                show_msg_2()
        else:
            show_msg_3()
