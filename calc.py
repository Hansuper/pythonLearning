#! /usr/bin/python
# -*-coding:utf-8 -*-
# input allow string
# 汉字
#name = input('please enter your name:')
#print('hello',name)
########

# s = r' hello,"bart" '
# print(s)
# b = r'''Hello,
# l'isa!'''
# print(b)
# ########

# a = 72.0
# b = 85.0
# c = (b-a)/a
# print('%.1f' % c)
# ######

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# ########

# age = input('how old are you:')
# if age < 18:
#     print('young')
# elif age >18 and age < 20:
#     print('adult')
# else:
#     print('old')
#     ##########

# hight = input('how hight:')
# weight = input('your weight:')
#
# bmi = weight / (hight*hight)
#
# if bmi < 18.5:
#     print('过轻')
# elif bmi >18.5 and bmi < 25:
#     print('正常')
# elif bmi >25 and bmi <28:
#     print('过重')
# elif bmi > 28 and bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')
#######

# a = 0
# for k in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     a = a + k
# print a
# #########


# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2 #可以尝试取消掉这个退出循环的条件－－死循环
# print sum
#
# L = ['jack','michal','jordan']
# for k in L:
#     print('hello,%s' % k)
#     ##############

# n = 1
# while n <= 10:
#     n = n+1
#     if n % 2 == 0:
#         continue
#     print n
##########


# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#         #######


# def pwer(x,n):
#     s = 1
#     while n > 0:
#         n = n-1
#         s = s * x
#     return s
#     #########
#


# def calc(*number):
#     sum = 0
#     for i in number:
#         sum = sum + i * i
#     return sum
#
# num = [1,2,3]
# print calc(*num)

# def person(name,age):
#     print ('name=%s,age=%s' %(name,age))
# person('harrod','22')
# #######
#

# def add_end(l=None):
#     if l is None:
#         l=[]
#     l.append('END')
#     return l
# print add_end()

#命名关键字参数
# def person(name,age,*,city,job):
#     print(name,age,city,job)
# person('jack',22,city='beijing',job='enger')
# ######
#args为可变参数
#kw 为关键字参数
# def f1(a,b,c=0,*args,**kw):
#     print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw
# f1(2,3)
# f1(2,3,4)
# f1(2,3,4,'a','b')
# f1(2,3,4,'a','b',x=99)
# #######


# def f2(a,b,c=0,*,d,**kw):
#     print 'a=',a,'b=',b,'c=',c,'d=',d
# f2(2,3,d=3)
# ######

# def fact(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     return fact_iter(num-1,num*product)

# l = []
# n = 1
# while n < 10 :
#     l.append(n)
#     n = n+2
# print l
#

# d = {'a':1,'b':2,'c':3}
# for k,v in d.items():
#     print(v,k)


# l = ['Jack','Macil','Haader',1,'Pen']
# [n.lower() for n in l if isinstance(n,str)]
#

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n+1
#     return 'done'
#
# fib(10)
##############


# def add(a,b,f):
#     return f(x)+f(b)
#

# def prod(l):
#     n = 1
#     for i in l:
#         n = n*i
#     return n
#
# print prod([3,4,5])
#

# def normalize(name):
#     w = []
#     s = [n.lower() for n in name if isinstance(n,str)]
#     for i in s:
#         w.append(i[:1].upper()+i[1:])
#     return w
#
# print normalize(['jaCk','MMed','edfF'])
#
#

def not_empty(s):
    return s and s.strip()
