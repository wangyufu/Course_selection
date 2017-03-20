#!/usr/bin/env python
from core.main import Admin
from core.main import School
from core.main import Course
from core.main import Classes
from core.main import Teacher
from core.main import Students


def create_school():
    try:
        print('创建学校'.center(60, '='))
        name = input('请输入学校名字: ').strip()
        addr = input('请输入学校地址: ').strip()
        school_name_list = [(obj.name, obj.addr) for obj in School.get_all_obj_list()]
        if (name, addr) in school_name_list:
            print('%s-%s,校区已存在' % (name, addr))
            return
        obj = School(name, addr)
        obj.save()
        print('%s-%s,校区创建成功' % (name, addr))
    except:
        print('选项不正确')


def show_school():
    for obj in School.get_all_obj_list():
        print('学校：%s    地址：%s   创建时间：%s' % (obj.name, obj.addr, obj.create_time))


def create_course():
    try:
        print('创建课程'.center(60, '='))
        school_list = School.get_all_obj_list()
        for k, obj in enumerate(school_list):
            print(k, obj.name, obj.addr)
        sid = int(input('请选择学校: '))
        school_obj = school_list[sid]

        name = input('请输入课程名: ').strip()
        price = input('请输入课程价格: ').strip()
        period = input('请输入课程周期: ').strip()

        course_name_list = [(obj.name, obj.school_nid.uuid) for obj in Course.get_all_obj_list()]
        if (name, school_obj.nid.uuid) in course_name_list:
            print('%s 课程已存在' % name)
            return
        obj = Course(name, price, period, school_obj.nid)
        obj.save()
        print('创建课程成功')
    except:
        print('选项不正确')


def show_course():
    for obj in Course.get_all_obj_list():
        print('课程名：%s   价格：%s   周期：%s   校区：%s，%s'
              % (obj.name, obj.price, obj.period, obj.school_nid.get_obj_by_uuid().name,
                 obj.school_nid.get_obj_by_uuid().addr))


def create_classes():
    try:
        print('创建班级'.center(60, '='))
        course_list = Course.get_all_obj_list()
        for k, obj in enumerate(course_list):
            print(k, obj.name, obj.school_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().addr)
        sid = int(input('请选择课程: '))

        course_obj = course_list[sid]

        name = input('请输入课班级名: ').strip()

        classes_name_list = [(obj.name, obj.course_nid.uuid) for obj in Classes.get_all_obj_list()]
        if (name, course_obj.nid.uuid) in classes_name_list:
            print('%s 班级以重复' % name)
            return
        obj = Classes(name, course_obj.nid, course_obj.school_nid)
        obj.save()
        print('创建课程成功')
    except:
        print('选项不正确')


def show_classes():
    for obj in Classes.get_all_obj_list():
        print('班级：%s   课程：%s    校区：%s，%s'
              % (obj.name, obj.course_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().name,
                 obj.school_nid.get_obj_by_uuid().addr))


def create_teacher():
    try:
        print('创建老师'.center(60, '='))
        scholl_list = School.get_all_obj_list()
        for k, obj in enumerate(scholl_list):
            print(k, obj.name, obj.addr)
        sid = int(input('请选择学校: '))

        scholl_obj = scholl_list[sid]

        for k, obj in enumerate(Classes.get_all_obj_list()):
            if str(scholl_obj.nid) == str(obj.school_nid):
                print('%s   班级：%s   课程：%s    校区：%s，%s'
                      % (k, obj.name, obj.course_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().name,
                         obj.school_nid.get_obj_by_uuid().addr))
        classes_list = Classes.get_all_obj_list()
        cid = int(input('请选择班级: '))
        classes_obj = classes_list[cid]

        name = input('请输入老师姓名: ').strip()

        teacher_name_list = [(obj.name, obj.classes_nid.uuid) for obj in Teacher.get_all_obj_list()]
        if (name, classes_obj.nid.uuid) in teacher_name_list:
            print('%s 老师信息以重复' % name)
            return
        obj = Teacher(name, classes_obj.nid)
        obj.save()
        print('创建老师信息成功')
    except:
        print('选项不正确')


def show_teacher():
    for obj in Teacher.get_all_obj_list():
        print('老师：%s   班级：%s    校区：%s，%s'
              % (obj.name, obj.classes_nid.get_obj_by_uuid().name,
                 obj.classes_nid.get_obj_by_uuid().school_nid.get_obj_by_uuid().name,
                 obj.classes_nid.get_obj_by_uuid().school_nid.get_obj_by_uuid().addr))


def create_student(_type='创建'):
    try:
        print(_type+'学生'.center(60, '='))
        scholl_list = School.get_all_obj_list()
        for k, obj in enumerate(scholl_list):
            print(k, obj.name, obj.addr)
        sid = int(input('请选择学校: '))
        scholl_obj = scholl_list[sid]

        for k, obj in enumerate(Classes.get_all_obj_list()):
            if str(scholl_obj.nid) == str(obj.school_nid):
                print('%s   班级：%s   课程：%s    校区：%s，%s'
                      % (k, obj.name, obj.course_nid.get_obj_by_uuid().name, obj.school_nid.get_obj_by_uuid().name,
                         obj.school_nid.get_obj_by_uuid().addr))
        classes_list = Classes.get_all_obj_list()
        cid = int(input('请选择班级: '))
        classes_obj = classes_list[cid]

        name = input('请输入学生姓名: ').strip()
        age = input('请输入学生年龄: ').strip()
        phone = input('请输入学生手机: ').strip()
        username = input('请输入学生账户: ').strip()
        password = input('请输入学生账户密码: ').strip()

        students_name_list = [(obj.phone, obj.classes_nid.uuid) for obj in Students.get_all_obj_list()]
        if (phone, classes_obj.nid.uuid) in students_name_list:
            print('%s 学生手机信息重复' % name)
            return
        obj = Students(name, age, phone, classes_obj.nid, username, password)
        obj.save()
        print('%s学生%s信息成功' % (_type, name))
    except:
        print('选项不正确')


def show_student():
    for obj in Students.get_all_obj_list():
        print('学生：%s   班级：%s    校区：%s，%s'
              % (obj.name, obj.classes_nid.get_obj_by_uuid().name,
                 obj.classes_nid.get_obj_by_uuid().school_nid.get_obj_by_uuid().name,
                 obj.classes_nid.get_obj_by_uuid().school_nid.get_obj_by_uuid().addr))


def show():
    msg = '''
        0:选项
        1:创建学校
        2:查看学校
        3:创建课程
        4:查看课程
        5:创建班级
        6:查看班级
        7:创建老师
        8:查看老师
        9:创建学生
        10:查看学生
        11:退出
    '''
    print(msg)


def main():
    choice_dic = {
        '0': show,
        '1': create_school,
        '2': show_school,
        '3': create_course,
        '4': show_course,
        '5': create_classes,
        '6': show_classes,
        '7': create_teacher,
        '8': show_teacher,
        '9': create_student,
        '10': show_student,
        '11': exit
        # '7': create_course_to_teacher,
    }
    show()
    while True:
        choice = input('请输入选项: ').strip()
        if choice not in choice_dic:
            continue
        choice_dic[choice]()


def login():
    username = input('请输入admin用户名：')
    password = input('请输入admin密码：')
    for admin in Admin.get_all_obj_list():
        if admin.username == username and admin.password == password:
            print('登录成功')
            main()
    else:
        print('用户名或密码错误')
        return
