from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split()
        fltLine=list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat
def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))
def randCent(dataSet,k):
    n=shape(dataSet)[1]
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids
def kMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroids=createCent(dataSet,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):
            minDist=inf;minIndex=-1
            for j in range(k):
                distJI=distMeas(centroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist=distJI;minIndex=j
            if clusterAssment[i,0]!=minIndex:clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
      #  print(centroids)
        for cent in range(k):
            ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=mean(ptsInClust,axis=0)
    return centroids,clusterAssment
def showCluster(datMat,centroids,clusterAssment,k):
    n=datMat.shape[0]
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    for i in range(n):
        o=int(clusterAssment[i,0])
        plt.plot(datMat[i,0],datMat[i,1],mark[o])
    mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    for i in range(k):
        plt.plot(centroids[i,0],centroids[i,1],mark[i],markersize=12)
    plt.show()
datMat=mat(loadDataSet('testSet.txt'))
myCentroids,clustAssing=kMeans(datMat,4)
showCluster(datMat,myCentroids,clustAssing,4)