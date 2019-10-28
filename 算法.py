def loadDataSet(filename):
    fr = open(filename)
    tot = 0
    for line in fr.readlines():
        curLine = line.strip().split()
        tot += 1
        if (tot == 1):
            n = int(curLine[0])
        else:
            a = list(map(int, curLine))
    return n,a
if __name__=='__main__':
    n, a = loadDataSet('fan.in')
    b = {}
    tot = 0
    ans = 0
    c = []#求一个组的第一个出现位置
    for i in range(n):
        x = a[i] // 2
        if (x in b):
            ans += i - b[x] - 1
            tot += len(c) - c.index(x) - 1
            c.remove(x)
        else:
            b[x] = b.get(x, i)
            c.append(x)
    print(ans - tot)