def loadDataSet(filename):
    fr=open(filename)
    tot=0
    for line in fr.readlines():
        curLine=line.strip().split()
        tot+=1
        if(tot==1):n=int(curLine[0])
        else:
            a=list(map(int,curLine))
    return n,a
if __name__=='__main__':
    n,a=loadDataSet('fan.in')
    b={};b1={};tot=0;ans=0
    l=[0 for i in range(100)]
    r = [0 for i in range(100)]
    c=[];c1=[]
    for i in range(n):
        x=a[i]//2
        if(x in b):
            ans+=i-b[x]-1
            l[x]=len(c)-c.index(x)-1
            tot+=l[x]
            c.remove(x)
        else:
            b[x] = b.get(x, i);
            c.append(x)
        """x = a[n-i-1] // 2
        if (x in b1):
            r[x] = len(c1) - c1.index(x) - 1
            if (l[x] != 0): tot += abs(l[x] - r[x])
            c1.remove(x)
        else:
            b1[x] = b1.get(x, i);
            c1.append(x)"""
    print(l)
    print(r)
    print(ans-tot)