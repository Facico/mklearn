from numpy import *
import operator
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split()
        fitLine=list(map(float,curLine[:3]))
        dataSet.append(fitLine)
        labelSet.append(curLine[-1:][0])
    return dataSet,labelSet
def dataProduce(dataSet):
    m,n=dataSet.shape
    dataSetN=dataSet.copy()
    for j in range(n):
        minx=min(dataSet[:,j])
        maxx=max(dataSet[:,j])
        for i in range(m):
            dataSetN[i,j]=(dataSet[i,j]-minx)/(maxx-minx)
    return dataSetN
def dataProduce1(dataSet):
    m,n=dataSet.shape
    dataSetN=dataSet.copy()
    mu=dataSet.mean(axis=0)
    delta=[]
    for j in range(n):
        o=0
        for i in range(m):
            o+=(dataSet[i,j]-mu[j])**2
        o/=m
        o=sqrt(o)
        delta.append(o)
    for j in range(n):
        for i in range(m):
            dataSetN[i,j]=(dataSet[i,j]-mu[j])/delta[j]
    return dataSetN
def classify(K):
    n=dataSet.shape[0]
    nn=testSet.shape[0]
    error=0
    for j in range(nn):
        MatB=tile(testSet[j],(n,1))-dataSet
        MatA=pow(MatB,2)
        distanceX=MatA.sum(axis=1)
        a=distanceX.argsort()
        countX={}
        for i in range(K):
            label=labelSet[a[i]]
            countX[label]=countX.get(label,0)+1
        countX=sorted(countX.items(),key=operator.itemgetter(1),reverse=True)
        if(countX[0][0]!=testLabel[j]):error+=1
    return (100.0-error)/100.0
if __name__=='__main__':
    dataSet,labelSet=loadDataSet('datingTestSet.txt')
    dataSet=array(dataSet)
    dataSetN=dataProduce1(dataSet)
    testSet=dataSetN[-100:];dataSet=dataSetN[:-100]
    testLabel = labelSet[-100:];labelSet = labelSet[:-100]
    maxx=0.0
    for K in range(1,21):
        maxx=max(classify(K),maxx)
    print(maxx)