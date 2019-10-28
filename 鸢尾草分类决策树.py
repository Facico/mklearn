from numpy import *
from math import log
import operator
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        try:
            curline=line.strip().split()
            furline=list(map(float,curline[:3]))
            dataSet.append(furline)
            labelSet=labelSet+curline[-1:]
        except ValueError:
            ans=1
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
    dataSetO,labelSetO=loadDataSet('datingTestSet.txt')
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