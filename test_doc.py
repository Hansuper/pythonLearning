#! /usr/local/bin/python3

try:
    f = open('file.txt','r')
    print(f.read())
    print('22')
finally:
    if f:
        f.close()
        print('close')
        
