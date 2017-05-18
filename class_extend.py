#! /usr/bin/python
# -*- coding:utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is runing...')



class Dog(Animal):
    def run(self):
        print('dog is runing')
    def eat(self):
        print('dog is eating')


class Cat(Animal):
    def run(self):
        print('cat is runing')


def run_twice(cs):
    cs.run()
    cs.run()

class Timer(object):
    def run(self):
        print('start....')
