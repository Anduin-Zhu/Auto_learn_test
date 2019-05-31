# -*- coding:utf-8 -*-
__author__ = '朱永刚'
import xlrd

user_file_path =r'E:\PycharmProject\Auto_learn_test\语言基础流程控制\登陆接口习题\user_file.xlsx'
#打开用户信息文件
user_file = xlrd.open_workbook('user_file.xlsx')
#输出所有sheet的名字
print(user_file.sheet_names())
#根据sheet索引或者名称获取sheet内容
data_sheet = user_file.sheets()[0]#通过索引获取
#data_sheet = user_file.sheet_by_name('Sheet1')#通过名称获取
#data_sheet = user_file.sheet_by_index(0)#通过索引获取
print(data_sheet)



 

'''
#定义一个列表来存放输入错误超过三次的人员
user_heimingdan_list = []

#主程序

while True:
    username_input = input("请输入您的用户名：")
    passwd_input = input("请输入您的密码：")
    for temp in user_heimingdan_list:
        if temp != username_input:
            pass
'''