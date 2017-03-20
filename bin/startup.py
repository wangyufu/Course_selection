#!/usr/bin/env python

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.services import initialize_service
from core.services import admin_service
from core.services import teacher_service
from core.services import student_service


def show_role():
    msg = '''
    0:初始化
    1:管理员
    2:老师(未实现)
    3:学生
    '''
    print(msg)

if __name__ == '__main__':
    role_main = {
        '0': initialize_service.main,
        '1': admin_service.login,
        # '2': teacher_service.login,
        '3': student_service.main,
    }
    while True:
        show_role()
        choice = input('输入角色: ').strip()
        if choice == 'q':
            exit('退出系统')
        if choice not in role_main:
            continue
        role_main[choice]()