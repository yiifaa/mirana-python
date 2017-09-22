# -*- coding : UTF-8 -*-
import types
from inspect import isfunction

class MetaClass(type):

    def __init__(self, cls, bases, attrs):
        # for key in attrs:
        #     print type(attrs[key])
        def isClass():
            return True
        #print isinstance(cls, str)
        #cls.isClass = isClass
        attrs['isClass'] = isClass
        #print attrs
        super(MetaClass, self).__init__(cls, bases, attrs)

class Root(object):
    __metaclass__ = MetaClass
    version = 1.0
    #__slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '''{{
                "name" : "{name}",
                "age" : "{age}"
               }}'''.format(name = self.name, age = self.age)
    
    def __getattribute__(self, attr):
        print '__getattr__:%s' %attr
        return object.__getattribute__(self, attr)
    
    def __getattr__(self, attr):
        print '__getattr__:%s' %attr
        if(attr in self.__dict__.keys()):
            return getattr(self, attr)
        return None

    def __get__(self, obj, type=None):
        print '__get__'
        return self

    def __getitem__(self, attr):
        print '__getitem__'
        return getattr(self, attr)

if __name__ == '__main__':
    add = lambda a, b: a + b
    # if(hasattr(add, '__call__')):
    #     print add(1,2)
    # if(isfunction(add)):
    #     print add(5, 5)
    # if(callable(add)):
    #     print add(2, 2)
    # if(isinstance(add, types.MethodType)):
    #     print add.__name__
    # print isinstance(add, types.MethodType)
    yiifaa = Root('yiifaa', 32)
    print yiifaa.version
    print yiifaa['name'] + 'item'
    print type(yiifaa).__dict__['name'].__get__(yiifaa, type(yiifaa))
    #print yiifaa.name
    #print yiifaa.__dict__['name']
    #print getattr(yiifaa, 'name')
    print yiifaa.username
    dict = {'user' : yiifaa}
    
    class X:
        user = yiifaa
    
    x = X()
    x.user
    #print Root.__dict__
    #print Root.__dict__['name'].__get__(yiifaa, Root)
    #yiifaa.comp = 'didi'
    #print type(yiifaa.__dict__).__dict__
    #yiifaa.isClass