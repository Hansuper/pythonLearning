#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

from hello_web import application

httpd = make_server('',8000,application)

print('server http on 8000.....')

httpd.serve_forever()
