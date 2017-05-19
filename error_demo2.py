#! /usr/bin/python

# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar('0')
#     except StandardError,e:
#         logging.exception(e)
#
# main()
# print 'END'

# def foo(s):
#     n = int(s)
#     return 10 / n
#
# def bar(s):
#     try:
#         return foo(s) * 2
#     except StandardError, e:
#         print 'Error!'
#         raise
#
# def main():
#     bar('0')
#
# main()


)

s = '0'
n = int(s)
print(10 / n)
