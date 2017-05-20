#! /usr/local/bin/python3

# import os
#
# def dir_l():
#     print([x for x in os.listdir('.')])
#
#
# def find_file(keyword,dir_name='.'):
#     for x in os.listdir(dir_name):
#         if x.__contains__(keyword):
#             print(os.path.join(dir_name,x))
#         if os.path.isdir(x):
#             find_file(keyword,os.path.join(dir_name,x))
#
#
# if __name__ == '__main__':
#     #dir_l()
#     find_file('txt')


import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def stodict(std):
    return {
        'name':std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('bob',20,43)
print(json.dumps(s,default=stodict))
