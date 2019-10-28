class sb:
    a=1
    b=1
    def run(self):
        print('sb')
class clf(sb):
    def run(self):
       print('haha')
class dog(clf):
    pass
def run_twice(x):
    x.run()
    x.run()
a=dog()
run_twice(a)
print(hasattr(a,'a'))
setattr(a,'c',10)
print(a.c)
"""print(type(a))
print(isinstance('1',(list,str)))

class student:
    _a='clf'
    _b='sb'
    def __init__(self,name,score):
        self.__name=name
        self._score=score
    def pr(self):
        print(self._a,self._b,self.__name,self._score)
    def get_name(self):
        print(self.__name)
a=student('clf',0)
a.__name='sb'
print(a.__name)
a.get_name()
print(a._student__name)"""