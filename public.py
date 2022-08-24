# ！/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
# @Time         :   2022/8/22 8:10
# @Author       :   Dominance
# @File         :   public.py
# @Version      :   V 1.0.0
# @Description  :   公共变量
'''
import os
import sys
'''------------------------------------------------------------------------------------------------------------------'''
if getattr(sys, 'frozen',None):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)
'''------------------------------------------------------------------------------------------------------------------'''
path = basedir
Generate_Sign = False