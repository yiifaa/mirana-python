#! /bin/bash/env python
# -*- coding : UTF-8 -*-

class Test:

    username = 'yiifaa'

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def sayHell(self, username, age):
        return self + username + age

    #@staticmethod
    def sayHello(cls):
        print cls
        
    sayHello = staticmethod(sayHello)    

    @classmethod
    def sayHi(cls):
        print cls


class Domain:
    version = 1.0

    def __init__(self, username, age):
        self.username = username
        self.age = age

domain1 = Domain('yiifaa', 32)
domain2 = Domain('yiifee', 30)
domain1.version = 2.0
print domain2.version

test = Test('yiifee', 32)
test.sayHello = 'YES'
test.username = 'yii'

print test.sayHello
print test.username
print Test.username

Test.sayHello(1)