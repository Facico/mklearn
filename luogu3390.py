import time
mo=int(1e9+7)
N=100
class node:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        d=node([[0 for j in range(N)] for i in range(N)])
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    d.a[i][j]=(self.a[i][k]*other.a[k][j]+d.a[i][j])%mo
        return d
    def __pow__(self,y):
        c=node([[0 for j in range(N)] for i in range(N)])
        for i in range(N):
            c.a[i][i]=1
        while y:
            if y&1:c=c*self
            self = self * self
            y//=2
        return c
"""f=open('fan.in','r')
o=-2
for s in f:
    o+=1
    if o==-1:
"""
#kong=[[0 for j in range(N)] for i in range(N)]

s=input().split()
n,k=int(s[0]),int(s[1])
N=n
a=node([[0 for j in range(N)] for i in range(N)])
for i in range(n):
    s=input().split()
    for j in range(n):
        a.a[i][j]=int(s[j])
t1=time.time()
a=a**k
for i in range(n):
    for j in range(n):
        print(a.a[i][j],end=' ')
    print('\n')
t2=time.time()
print(t2-t1,"s")


