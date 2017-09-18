# -*- coding:UTF-8 -*-
from string import Template

def format(**args):
    tmpl = 'My name is %(username)s, age is %(age)d!'    
    return str(tmpl % args)

def format_2(**args):
    tmpl = 'My name is ${username}, age is ${age}!' 
    #tmpl = 'select * from user where username = ${username} and password = ${password}'
    # 强烈建议使用
    return Template(tmpl).safe_substitute(args) 
    #return Template(tmpl).substitute(args)


print(format(username='username', age= 32))
#  这样即使少个参数也不影响
print(format_2(username='username', age= 32))