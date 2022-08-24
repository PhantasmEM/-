# ！/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
# @Time         :   2022/8/24 8:52
# @Author       :   Dominance
# @File         :   cmd.py
# @Version      :   V 1.0.0
# @Description  :   
'''

import subprocess


def cmd(command):
    try:
        subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
    except Exception as e:
        print(e)