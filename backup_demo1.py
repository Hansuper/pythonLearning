#! /usr/bin/python
#filename backup_demo1.py 

import os
import time

source = ['/Users/name/data/code','/Users/name/data/dev/blog']

target_dir = '/Users/name/data'
target = target_dir + time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command = "zip-qr'%s' %s"%(target_dir,' '.join(source))
# print zip_command

if os.system(zip_command) == 0:
	print 'success'
else:
	print 'fail'