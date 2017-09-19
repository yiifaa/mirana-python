# -*- coding:UTF-8 -*-

# 位置参数与命名参数
import types

def add(*items, **args):
    result = 0
    for item in items:
        result = result + item
    
    if(args != None):
        for key in args.keys():
            result = result + args[key]

    return result

class Math:
    def __init__(self):
        #self.add = lambda a, b: a + b
        pass
        #add = lambda s, a, b: a + b
        #self.add = types.MethodType(add, self)

    @classmethod
    def addInt(cls, a, b):
        return a + b    

Math.add = types.MethodType(lambda c, a, b: a + b, Math)
#Math.add = lambda s, a, b: a + b

m = Math()
#math.add = lambda a, b: a + b
print Math.add(1,2) 
# #Person.addInt = lambda self,a, b : a + b
# addInt = lambda self,a, b : a + b

# yiifaa = Person()
# yiifaa.addInt = types.MethodType(addInt, yiifaa, Person)
# yiifaa.__num__ = 100


# yiifee = Person()

# //print yiifee.addInt(2,3)
# print yiifaa.__num__
# print yiifaa.addInt(1, 2)
# print add(1, 2, 3, 4, last = 5)