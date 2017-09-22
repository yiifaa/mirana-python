# -*- coding:UTF-8 -*-

# pylint: disable=C1001
class Base(object):
    version = 1.0

    def __init__(self, username, age):
        self.username = username
        self.age = age


class Employee(Base):
    
    def __init__(self, username, age):
        print username
        super(Employee, self).__init__(username, age)

yiifaa = Employee('yiifaa', 32)
print yiifaa.version
print yiifaa.username