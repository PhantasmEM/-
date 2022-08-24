# ！/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
# @Time         :   2022/8/22 10:42
# @Author       :   Dominance
# @File         :   operation.py
# @Version      :   V 1.0.0
# @Description  :   操作
'''
from Common.cmd import cmd

# 断网
def off():
    cmd('netsh advfirewall firewall set rule name="hh_ldp" new enable=yes')

# 恢复网络
def reconnection():
    cmd('netsh advfirewall firewall set rule name="hh_ldp" new enable=no')


# 添加路径，生成程序
def add(path):
    cmd(r'netsh advfirewall firewall add rule name="hh_ldp"  dir=out enable=no'
              r'  program="{}"  action=block'.format(path))

# 删除规则
def delete():
    cmd('netsh advfirewall firewall delete rule name="hh_ldp"')