#!/usr/bin/env python
from core.main import Admin

def main():
    username = input('请输入admin用户名：').strip()
    password = input('请输入admin密码：').strip()
    obj = Admin(username, password)
    obj.save()
    for admin in obj.get_all_obj_list():
        if admin.username == username:
            print('创建成功')
            return
        else:
            print('创建失败')