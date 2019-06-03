# -*- coding:utf-8 -*-
__author__ = '朱永刚'

import sys
'''
user_file_path =r'E:\PycharmProject\Auto_learn_test\语言基础流程控制\登陆接口习题\\user_file.xlsx'


#打开用户信息文件
user_file = xlrd.open_workbook('user_file.xlsx')
#输出所有sheet的名字
print(user_file.sheet_names())
#根据sheet索引或者名称获取sheet内容
data_sheet = user_file.sheets()[0]#通过索引获取
#data_sheet = user_file.sheet_by_name('Sheet1')#通过名称获取
#data_sheet = user_file.sheet_by_index(0)#通过索引获取
#获取sheet名称
print(data_sheet.name)
row_num = data_sheet.nrows#获取行数
col_num = data_sheet.ncols#获取列数
print(row_num,col_num)
#获取所有单元格内容
list = []
for i in range(row_num):
    row_list = []
    for j in range(col_num):
        row_list.append(data_sheet.cell_value(i,j))
    list.append(row_list)
print(list)

#获取第一行内容
rows = data_sheet.row_values(0)
print(rows)
#获取第二列内容
cols = data_sheet.col_values(1)
print(cols)
print(data_sheet.cell_value(2,0))


#定义一个列表来存放输入错误超过三次的人员
user_heimingdan_list = []

#主程序
user_file = xlrd.open_workbook('user_file.xlsx')
data_sheet = user_file.sheets()[0]
list = []
for i in range(data_sheet.nrows):
    row_list = []
    for j in range(data_sheet.ncols):
        row_list.append(data_sheet.cell_value(i,j))
    list.append(row_list)
print(list)


while True:
    username_input = input("请输入您的用户名：")
    passwd_input = input("请输入您的密码：")
    for temp in list:
        print(type(temp[1]))
        if temp[0] == username_input:
            if temp[1] == passwd_input:
                print(type(temp[1]))
                for i in user_heimingdan_list:
                    if i != username_input:
                        print("登录成功")
                    else:
                        print("您已输入错误超过三次，请联系管理员")
                        continue
            else:
                print("密码输入错误")
                continue
        else:
            print("用户名输入错误")
            continue
'''

account_file = 'account.txt'
account_look_file = 'account_lock.txt'
retry_count = 0
retry_limit = 3

while retry_count < retry_limit:
    username = input("请输入你的用户名")
    lock_check = open(account_look_file)
    for line in lock_check.readlines():
        if username == line.strip():#检查是否在黑名单中
            print("账号已被锁定")
            sys.exit()
    password = input("请输入你的密码：")
    f = open(account_file)
    math_flag = False#设置一个变量用来记录登录状态
    for line in f.readlines():
        user,passwd = line.strip().split()#去掉每行多余的换行，并把每一行按空格分割，分别赋值个user和passwd
        if user == username and passwd == password:
            print("欢迎%s,登录成功！！"%username)
            math_flag = True#登录成功后状态改变
            sys.exit()
    f.close()
    if math_flag == False:#如果为false表示未登录成功
        retry_count += 1

else:
    print("你的账号已被锁定")
    f = open(account_look_file,'a')
    f.write(username + '\n')
    f.close()