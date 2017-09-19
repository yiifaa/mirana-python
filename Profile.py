#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import types

class Profiled:
    def __init__(self, func):
        self.func = func
        self.calls = 0
    
    def __call__(self, *args, **xargs):
        self.calls += 1
        return self.func(*args, **xargs)
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

class AddDeco:    
    def __init__(self, cls):
        self.cls = cls
        self.calls = 0
        cls.count = lambda cls : self.calls

    def __call__(self, *args, **xargs):
        self.calls = self.calls + 1
        print 'called %x times' %self.calls
        return self.cls(*args, **xargs)


def addDeco(cls):
    def add(c, a, b):
        return a + b
    cls.add = add
    return cls

def instCounter(cls):
    oldInit = cls.__init__
    counter = [0]
    def newInit(self, *args, **xargs):
        #global counter
        counter[0] = counter[0] + 1
        oldInit(self, *args, **xargs)

        #nonlocal是在Python3.0中新增的关键字
        #nonlocal counter
        #counter = value
    
    #newInit.get_counter = get_counter
    #newInit.set_counter = set_counter


    cls.__init__ = newInit
    cls.count = types.MethodType(lambda c: counter[0], cls)
    return cls

@addDeco
class Math:
    pass

@instCounter
#@AddDeco
class Test:
    def __init__(self):
        pass


@Profiled
def add(x, y):
    return x + y

print add(2, 3)
print add.calls

math = Math()
print math.add(1, 2)

for i in range(1,10,1):
    Test()
print Test.count()
#print t.calls