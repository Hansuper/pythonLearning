#! /usr/bin/python
# -*- coding:utf-8 -*-

'class private'

class Student(object):
    def __init__(self,name,score):
        # 两个下划线开头的变量名表示为私有变量外部不能访问
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))



# >>> a = student('kobe','24')
# >>> a.__name 报错外部不能访问可以新增一个方法

    def get_name(self):
        return self.__name

# >>> a.__name = 'west' 虽然可以设置成功，但是调用get_name方法时返回的还是kobe
# 如果非要访问可以使用 a._Student__name 但最好不要这样用
