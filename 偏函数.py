import functools as clf
print(int('12345',base=8))
int8=clf.partial(int,base=8)
print(int8('12345'))
max2=clf.partial(max,10)
print(max2(1,2,3))