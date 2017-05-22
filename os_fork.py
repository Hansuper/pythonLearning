#! /usr/local/bin/python3
# -*- coding:utf-8 -*-

# import os
#
# print('process(%s) start..' % os.getpid())
#
# pid = os.fork()
#
# if pid == 0:
#     print('child process (%s),my partent (%s)' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s)' % (os.getpid(),pid))


# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('exit code:',r)

# from multiprocessing import Process,Queue
# import os,time,random
#
# def write(q):
#     print('process to write %s' % os.getpid())
#     for value in ['A','B','C']:
#         print('put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# def read(q):
#     print('process to read %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('get %s from queue' % value)
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()


# import time,threading
#
# def loop():
#     print('thread %s is running..' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n+1
#         print('thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('thread %s is running..' % threading.current_thread().name)
#
# print('thread %s is running..' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)


import time,threading

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
        change_it(n)
        finally:
            locak.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
