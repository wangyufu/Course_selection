#!/usr/bin/env python
from core.main import School
from core.main import Classes
from core.main import Students
from core.services import admin_service


def register():
    admin_service.create_student('注册')


def login():
    username = input('请输入学生用户名：')
    password = input('请输入学生密码：')
    for obj in Students.get_all_obj_list():
        user = obj.get_user()
        if user['username'] == username and user['password'] == password:
            print('登录成功'.center(60, '*'))
            menu(obj)
            return

    print('用户名或密码错误')


def pay_tuition(user_obj):
    if user_obj.get_tuition() == 10000:
        print('已交款')
        return
    tuition = int(input('输入交款金额：'))
    if tuition == 10000:
        user_obj.pay_tuition(tuition)
        user_obj.save()
        print('交款完成')
    else:
        print('交款金额不匹配')


def menu(user_obj):
    msg = '''
        0:交学费
        1:退出
    '''
    choice_dic = {
        '0': pay_tuition,
        '1': exit
    }
    while True:
        print(msg)
        choice = input('请输入选项: ').strip()
        if choice not in choice_dic:
            continue
        choice_dic[choice](user_obj)


def show():
    msg = '''
        0:选项
        1:注册
        2:登录
        3:退出
    '''
    print(msg)


def main():
    choice_dic = {
        '0': show,
        '1': register,
        '2': login,
        '3': exit
        # '7': create_course_to_teacher,
    }
    show()
    while True:
        choice = input('请输入选项: ').strip()
        if choice not in choice_dic:
            continue
        choice_dic[choice]()
