#! /usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'harrod'

# 类名通常首字母大写，object 代表是从哪个类
# 继承下来的，如果没有继承就写object，这是所有
# 类最终都会继承的类  

class Student(object):
    # __init__第一个参数永远是self,表示创建的实例本身
    # name,score这两个参数在实例化的时候  就必须传入了
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s 的成绩是%s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            print 'A'
        elif self.score >= 60:
            print 'B'
        else:
            print 'C'
