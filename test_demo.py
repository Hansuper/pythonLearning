#! /usr/local/bin/python3


def calc(*numbers):
    print(numbers)
    sume = 0
    for i in numbers:
        sume = i+sume
    print(sume)

a = (1,2,3,4)
#calc(*range(30))

def person(name,age,**kw):
    print(kw)
    print(name,'---',age,'---',kw)

other = {'city':'beijing','country':'chain'}
# person('jack',22,city='beijing',country = 'chain')
# person('jack',22,**other)

def person(name,age,*,city,job):
    print(city,job)

# person('jack',22,city='beijing',job='it',c='ee')

def fact(x):
    if x == 0:
        return 0
    return x + fact(x-1)

print(fact(10))
