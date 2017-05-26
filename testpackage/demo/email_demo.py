#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,adr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))



from_addr = input('From:')
password = input('Password:')
to_addr = input('To:')
smtp_server = input('SMTP server:')


msg = MIMEText('hello,send by python..','plain','utf-8')

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server_quit()
