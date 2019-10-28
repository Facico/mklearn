"""from numpy import *
import operator
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split(',')
        if ('id' in line): continue
        fitLine=list(map(float,curLine[2:32]))
        dataSet.append(fitLine)
        labelSet.append(curLine[1])
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
    dataSet,labelSet=loadDataSet('data.csv')
    dataSet=array(dataSet)
    dataSetN=dataProduce(dataSet)
    testSet=dataSetN[-100:];dataSet=dataSetN[:-100]
    testLabel = labelSet[-100:];labelSet = labelSet[:-100]
    maxx=0.0
    for K in range(1,21):
        maxx=max(classify(K),maxx)
    print(maxx)
"""
from numpy import *
from math import log
import operator
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split(',')
        if ('id' in line): continue
        fitLine=list(map(float,curLine[2:32]))
        dataSet.append(fitLine)
        labelSet.append(curLine[1])
    return dataSet,labelSet
def calcShonnonEnt(labelSet):
    classN={}
    n=len(labelSet)
    for i in range(n):
        label=labelSet[i]
        classN[label]=classN.get(label,0)+1
    Ent=0.0
    for key in classN.keys():
        gailv=float(classN[key]/n)
        Ent-=gailv*log(gailv,2)
    return Ent
def majority(labelSet):
    classN = {}
    n = len(labelSet)
    for i in range(n):
        label = labelSet[i]
        classN[label] = classN.get(label, 0) + 1
    classS=sorted(classN.items(),key=operator.itemgetter(1),reverse=True)
    return classS[0][0]
def splitData(dataSet,labelSet,feat,value):
    labA=[];matA=mat([]);labB=[]
    if(len(nonzero(dataSet[:,feat]<value))>0):
        for i in nonzero(dataSet[:,feat]<value)[0]:
            labA.append(labelSet[i])
        matA=dataSet[nonzero(dataSet[:,feat]<value)[0],:]
    for i in nonzero(dataSet[:, feat] >= value)[0]:
        labB.append(labelSet[i])
    matB=dataSet[nonzero(dataSet[:,feat]>=value)[0],:]
    return matA,matB,labA,labB
def choosesplit(dataSet,labelSet,ops=(0,3)):
    if (labelSet.count(labelSet[0]) == len(labelSet)):
        return None, labelSet[0]
    if (dataSet.shape[1] == 1):
        return None, majority(labelSet)
    bestFeat=bestValue=0;bestS=inf
    n,m=dataSet.shape
    for j in range(m):
        aa=dataSet[:,j].tolist()
        bb=[i for item in aa for i in item]
        nSet=set(bb)
        for i in nSet:
            if(i==max(nSet))or(i==min(nSet)):continue
            matA, matB, labA, labB=splitData(dataSet,labelSet,j,i)
            probA=float(len(labA)/len(labelSet));
            probB = float(len(labB) / len(labelSet));
            splitEnt=probA*calcShonnonEnt(labA)+probB*calcShonnonEnt(labB)
            if(splitEnt<bestS):
                bestS=splitEnt
                bestFeat=j
                bestValue=i
    curvalue=calcShonnonEnt(labelSet)
    if(curvalue-bestS<ops[0]):
        return None,majority(labelSet)
    matA, matB, labA, labB = splitData(dataSet, labelSet, bestFeat, bestValue)
    if(shape(matA)[0]<ops[1])or(shape(matB)[0]<ops[1]):
        return None,majority(labelSet)
    return bestFeat,bestValue
def createTree(dataSet,labelSet):
    feat,val=choosesplit(dataSet,labelSet)
    if(feat==None):
        return val
    TreeX = {}
    TreeX['feat']=feat
    TreeX['val']=val
    matA, matB, labA, labB = splitData(dataSet, labelSet, feat, val)
    TreeX['left']=createTree(matA,labA)
    TreeX['right'] = createTree(matB, labB)
    return TreeX
def classify(dataX,TreeX):
    if('feat' not in TreeX):
        return TreeX
    feat=TreeX['feat'];val=TreeX['val']
    if(dataX[0,feat]<val):
        return classify(dataX,TreeX['left'])
    else:
        return classify(dataX,TreeX['right'])
if __name__=='__main__':
    dataSetO,labelSetO=loadDataSet('data.csv')
    dataSetO=mat(dataSetO);
    fen=100
    testSet = dataSetO[-fen:];dataSet = dataSetO[:-fen]
    testLabel = labelSetO[-fen:];labelSet = labelSetO[:-fen]
    myTree=createTree(dataSet,labelSet)
    print(myTree)
    error=0
    for i in range(len(testLabel)):
        u=classify(testSet[i],myTree)
        if(u!=testLabel[i]):error+=1
    print(float(fen-error)/fen)
