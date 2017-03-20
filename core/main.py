#!/usr/bin/env python
import os
import pickle
import time
from core import identifier
from conf import settings


class Base:
    def save(self):
        file_path = os.path.join(self.db_path, str(self.nid))
        pickle.dump(self, open(file_path, 'wb'))

    @classmethod
    def get_all_obj_list(cls):
        ret = []
        for filename in os.listdir(cls.db_path):
            file_path = os.path.join(cls.db_path, filename)
            ret.append(pickle.load(open(file_path, 'rb')))
        return ret


class Admin(Base):
    db_path = settings.ADMIN_DB_DIR

    def __init__(self, username, password):
        self.nid = identifier.AdminNid(self.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')


class School(Base):
    db_path = settings.SCHOOL_DB_DIR

    def __init__(self, name, addr):
        self.nid = identifier.SchoolNid(self.db_path)
        self.name = name
        self.addr = addr
        self.create_time = time.strftime('%Y-%m-%d %X')


class Course(Base):
    db_path = settings.COURSE_DB_DIR

    def __init__(self, name, price, period, school_nid):
        self.nid = identifier.CourseNid(self.db_path)
        self.name = name
        self.price = price
        self.period = period
        self.school_nid = school_nid


class Classes(Base):
    db_path = settings.CLASSES_DB_DIR

    def __init__(self, name, course_nid, school_nid):
        self.nid = identifier.ClassesNid(self.db_path)
        self.name = name
        self.course_nid = course_nid
        self.school_nid = school_nid
        self.create_time = time.strftime('%Y-%m-%d %X')


# class ClassRecord(Base):
#     def __init__(self, classes_nid, ):
#         self.classes_nid = classes_nid
#         self.record_time = time.strftime('%Y-%m-%d %X')


# class StudyRecord(Base):
#     def __init__(self, classes, course_num, record_time):
#         self.classes = classes
#         self.course_num = course_num
#         self.record_time = record_time


class Score:
    def __init__(self, nid):
        self.nid = nid
        self.score_dict = {}

    def set(self, course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self, course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid)


# class Score():
#     def __init__(self,nid):
#         self.nid=nid
#         self.score_dict={}


class Teacher(Base):
    db_path = settings.TEACHER_DB_DIR

    def __init__(self, name, classes_nid):
        self.nid = identifier.TeacherNid(self.db_path)
        self.name = name
        self.classes_nid = classes_nid
        self.create_time = time.strftime('%Y-%m-%d %X')


class Students(Base):
    db_path = settings.STUDENT_DB_DIR

    def __init__(self, name, age, phone, classes_nid, username, password, ):
        self.nid = identifier.StudentNid(self.db_path)
        self.name = name
        self.age = age
        self.phone = phone
        self.classes_nid = classes_nid
        self._username = username
        self._password = password
        self._tuition = 0
        self.score = Score(self.nid)

    def get_user(self):
        return {'username': self._username, 'password': self._password}

    def pay_tuition(self, tuition):
        self._tuition = tuition
        return self._tuition

    def get_tuition(self):
        return self._tuition
