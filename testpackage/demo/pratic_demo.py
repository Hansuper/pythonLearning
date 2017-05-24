#! /usr/local/bin/python3
# -*- coding:utf-8 -*-
#

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1,f2,f3 = count()
#
# print(f1())
# print(f2())
# print(f3())

# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
# @log
# def now():
#     print('hello word')

import functools


def log(*text):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s--begain-- %s' % (*text,func.__name__))
            #return func(*args,**kw)
            func(*args,**kw)
            print('end')
        return wrapper
    return decorator

@log()
def now():
    print('jjj')

now()
