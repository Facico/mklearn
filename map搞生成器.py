def g():
    o=1
    yield o
    while o<=10:
        o+=1
        yield o
def f(x):
    return x*x
b=map(f,g())
print(list(b))