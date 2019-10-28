from numpy import *
import matplotlib.pyplot as plt
def loadDataSet():
    dataMat = random.rand(100, 10)
    return mat(dataMat)
def dist(A,B):
    return sqrt(sum(power(A - B, 2)))
def randCent(dataSet,k):#随机初始质心
    n = dataSet.shape[1]
    centX = mat(zeros((k, n)))
    for j in range(n):
        rangeX = float(max(dataSet[:, j]) - min(dataSet[:, j]))
        centX[:, j] = min(dataSet[:, j]) + rangeX * random.rand(k, 1)
    return centX
def kMeans(dataSet,k):
    m = dataSet.shape[0]
    centClassify = mat(zeros((m, 2)))
    Zcent = randCent(dataSet, k)
    pan = 1
    while pan:
        pan = 0
        for i in range(m):
            minDist = inf
            minIndex = -inf
            for j in range(k):
                distX = dist(Zcent[j, :], dataSet[i, :])
                if (distX < minDist):
                    minDist = distX;
                    minIndex = j
            if (centClassify[i, 0] != minIndex): pan = 1
            centClassify[i, :] = minIndex, minDist ** 2
        for i in range(k):
            a = dataSet[nonzero(centClassify[:, 0].A == i)[0]]
            Zcent[i, :] = mean(a, axis=0)
    return Zcent, centClassify
if __name__ == '__main__':
    K = 2
    dataSet = loadDataSet()
    ZCent, centClassify = kMeans(dataSet, K)#ZCent表示质心，centClassify表示属于哪个簇