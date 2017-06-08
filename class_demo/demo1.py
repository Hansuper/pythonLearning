#! /usr/local/bin/python3
# -*- coding:utf8 -*-

# class Student(object):
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s : %s' % (self.__name,self.__score))
#
# bart = Student('bart simpson',40)
#
# print(bart.__name)


# class Student(object):
#     __slots__ = ('name','age')
#
# class Grade(Student):
#     #__slots__ = ('score')
#     pass
#
# g = Grade()
# g.score = 'hhh'


# s = Student()
# # s.name = 'jack'
# # print(s.name)
#
# def set_age(self,age):
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age,s)
# s.set_age(23)
# print(s.age)



# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('intint')
#         if value < 0 or value > 100:
#             raise ValueError('0-100')
#         self._score = value
#
# s = Student()
# s.score = 60
# print(s.score)


# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2017-self._birth


# class Student(object):
#     def __init__(self,name):
#         self._name = name
#
#     def __str__(self):
#         return 'studnet object (name: %s)' % self._name
#
# print(Student('jack'))


# class Fib(object):
#     def __init__(self):
#         self._a,self._b = 0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self._a,self._b = self._b,self._a + self._b
#         if self._a > 10:
#             raise StopIteration()
#         return self._a
#
# for n in Fib():
#     print(n)



# class Fib(object):
#     def __getitem__(self,n):
#         a,b = 1,1
#         for x in range(n):
#             a,b = b,a+b
#         return a
#
# print(Fib()[10])


# class Fib(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b = 1,1
#             for x in range(n):
#                 a,b = b,a+b
#             return a
#         if isinstance(n,slice):
#             start = n.start
#             stop  = n.stop
#             if start is None:
#                 start = 0
#             a,b = 1,1
#             l = []
#             for x in range(stop):
#                 if x >= start:
#                     l.append(a)
#                 a,b = b,a+b
#             return l
#
# print(Fib()[5:10])



# class Student(object):
#     def __getattr__(self,attr):
#         if attr == 'age':
#             return 25
#
# print(Student().a)


# class Student(object):
#     def __init__(self,name):
#         self._name = name
#
#     def __call__(self):
#         print('my name is %s' % self._name)
#
# s = Student('jack')
# s()

# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#
#     def __getattr__(self,path):
#         return Chain('%s/%s' % (self._path,path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().status.user.list.name)


from enum import Enum

Moth = Enum('Month',('Jan','Feb','Mar','Apr','May'))
for name,member in Moth.__members__.items():
    print(name,'=>',member,',',member.value)
