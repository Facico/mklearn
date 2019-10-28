def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield a,b
        a, b = b, a + b
        n = n + 1
class clf:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
b=iter(clf())
a=(i for i in range(1,103) if i%3==0)
d=zip(fib(6),a)
for i in d:
    print(i)