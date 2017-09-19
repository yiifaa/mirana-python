#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from functools import wraps

def after (num):
    def afterProxy(func):
        @wraps(func)
        def addMore (*args):
            result = func(* args) + num
            return result
        return addMore
    return afterProxy

def round(func):
    @wraps(func)
    def roundProxy(*args):
        print 'before execute'
        print func(*args)
        print 'end execute'
    return roundProxy

def before(func):
    @wraps(func)
    def check(a, *args):
        # 如果小于0，抛出异常
        if(a < 0):
            raise Exception(u'第一个参数小于0')
        else:
            return func(a, *args)
    return check


@round
@after(5)
@before
def add (a, b):
    return a + b

@before
def sub(a, b):
    return a + b


def mathExcept(ex):
    def exceptProxy(func):
        def divFunc(*args):
            try:
                return func(*args)
            except ex:
                return 0
        return divFunc
    return exceptProxy

@mathExcept(ZeroDivisionError)
def div(a, b):
    if(b == 0):
        raise ZeroDivisionError('b is zero')
    else:
        return a / b


print(sub.__name__)
#   print(sub.__)

# if(addSrc != None):
#     print addSrc(1, 2)

add(1, 2)
print div(3, 0)