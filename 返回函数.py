def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
a=count()
for i in range(0,3):
    print(a[i]())
