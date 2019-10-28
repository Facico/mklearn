"""import functools
f=abs
print(f(-1))
def fang(x):
    return x*x
a=map(fang,[1,2,3,4,5,6,7])
print(list(a))
def add(x,y):
    return x+y
b=functools.reduce(add,[1,2,3,4,5])
print(b)"""
from functools import *
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int('13511'))