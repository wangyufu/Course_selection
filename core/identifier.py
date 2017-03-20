#!/usr/bin/env python

from lib import commons
import os,pickle


class Nid:
    def __init__(self, db_path):
        self.uuid = commons.create_uuid()
        self.db_path = db_path

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        for filename in os.listdir(self.db_path):
            if filename == self.uuid:
                return pickle.load(open(os.path.join(self.db_path,filename),'rb'))
        return None


class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__(db_path)


class SchoolNid(Nid):
    def __init__(self, db_path):
        super(SchoolNid, self).__init__(db_path)


class TeacherNid(Nid):
    def __init__(self, db_path):
        super(TeacherNid, self).__init__(db_path)


class CourseNid(Nid):
    def __init__(self, db_path):
        super(CourseNid, self).__init__(db_path)


class Course_to_teacherNid(Nid):
    def __init__(self, db_path):
        super(Course_to_teacherNid, self).__init__(db_path)


class ClassesNid(Nid):
    def __init__(self, db_path):
        super(ClassesNid, self).__init__(db_path)


class StudentNid(Nid):
    def __init__(self, db_path):
        super(StudentNid, self).__init__(db_path)
