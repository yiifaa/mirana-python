# -*- coding:utf-8 -*-
import types
class Employee(object):

    def __init__(self, username, age):
        self.username = username
        self.age = age

    
  

    def __getattribute__(self, attr):
        return super(Employee, self).__getattribute__(attr)

    def __getitem__(self, attr):
        return super(Employee, self).__getattribute__(attr)

    def __getattr__(self, attr):
        return None



class Dept(object):

      def __init__(self, name):
          self.name = name
    
      def __get__(self, obj, type=None):
        print id(obj)
        return 'Dept'

class Company(object):
    dept = Dept('organ')

    

if __name__ == '__main__':
    em = Employee('yiifaa', 32)
    print em.company
    print em.username
    print em['username']

    class X:
        pass
        #dept = Dept()
    dept = Dept('OK')
    x = Company()
    print type(x.dept) == str