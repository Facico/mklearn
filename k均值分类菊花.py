from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(filename):#读文件
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        try:
            curLine=line.strip().split(',')
            fitLine=list(map(float,curLine[:4]))
            dataSet.append(fitLine)
            labelSet.append(curLine[-1:][0])
        except ValueError:
            pass
    return dataSet,labelSet
"""def splitDataSet(dataSet,labelSet,prob=0.6):
    dataSetN=[];labelSetN=[]
    testSet=[];testLabel=[]
    n=len(dataSet)
    for i in range(n):
        o=random.random()
        if(o<prob):
            dataSetN.append(dataSet[i]);labelSetN.append(labelSet[i])
        else:
            testSet.append(dataSet[i]);testLabel.append(labelSet[i])
    return mat(dataSetN),labelSetN,mat(testSet),testLabel"""
def dist(A,B):
    return sqrt(sum(power(A-B,2)))
def randCent(dataSet,k):#随机初始质心
    n = dataSet.shape[1]
    centX = mat(zeros((k, n)))
    for j in range(n):
        rangeX = float(max(dataSet[:, j]) - min(dataSet[:, j]))
        centX[:, j] = min(dataSet[:, j]) + rangeX * random.rand(k, 1)
    return centX
def kMeans(dataSet,labelSet,k):
    m = dataSet.shape[0]
    centClassify = mat(zeros((m, 2)))
    ZCent = randCent(dataSet, k)
    pan = 1
    while pan:
        pan = 0
        for i in range(m):
            minDist = inf
            minIndex = -inf
            for j in range(k):
                distX = dist(ZCent[j, :], dataSet[i, :])
                if (distX < minDist):
                    minDist = distX;
                    minIndex = j
            if (centClassify[i, 0] != minIndex): pan = 1
            centClassify[i, :] = minIndex, minDist ** 2
        for i in range(k):
            a = dataSet[nonzero(centClassify[:, 0].A == i)[0]]
            ZCent[i, :] = mean(a, axis=0)
    ZClassify = {}
    for i in range(k):
        countX = {}
        for j in range(m):
            if (centClassify[j, 0] == i): countX[labelSet[j]] = countX.get(labelSet[j], 0) + 1
        for x, y in countX.items():
            maxK = x;
            maxx = y
            break
        for x, y in countX.items():
            if (y > maxx):
                maxx = y
                maxK = x
        ZClassify[i] = maxK
    return ZCent,ZClassify,centClassify
def showClassify(dataSet,cent,centClassify,k):
    n=dataSet.shape[0]
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(n):
        o=int(centClassify[i,0])
        plt.plot(dataSet[i,0],dataSet[i,1],mark[o])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
        plt.plot(cent[i,0],cent[i,1],mark[i],markersize=12)
    plt.show()
def classify(ZCent,ZClassify,testSet,testLabel,k):
    m=testSet.shape[0]
    error=0
    for i in range(m):
        minDist = inf
        minIndex = -inf
        for j in range(k):
            distX = dist(ZCent[j, :], testSet[i, :])
            if (distX < minDist):
                minDist = distX;
                minIndex = j
        if(ZClassify[minIndex]!=testLabel[i]):error+=1
    return float((m-error)/m)
if __name__=='__main__':
    K=3
    dataSetOld,labelSetOld=loadDataSet('iris.data')
    #dataSet,labelSet,testSet,testLabel=splitDataSet(dataSetOld,labelSetOld)
    dataSet=mat(dataSetOld)
    labelSet=labelSetOld
    ZCent, ZClassify,centClassify = kMeans(dataSet, labelSet,K)
    print(classify(ZCent,ZClassify,dataSet,labelSet,K))#ZCent表示质心，centClassify表示属于哪个簇
    #showClassify(dataSet, ZCent, centClassify, K)