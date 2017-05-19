#! /usr/bin/python
# -*- coding:utf-8 -*-


# try:
# 	print('try....')
# 	r = 10/2
# 	print('result:',r)
# except ZeroDivisionError as e:
# 	print('except:',e)
# except ValueError, e:
# 	print 'valaueerrorr',e
# else:
# 	print 'no error'
# finally:
# 	print('finally...')
# print('end')
#


def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s)*2

def main():
	bar('0')
	# try:
	# 	bar('0')
	# except StandardError,e:
	# 	print 'Error'
	# finally:
	# 	print 'finally...'

main()
