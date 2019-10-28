from numpy import *
import operator
from math import *
def loadDataSet(filename):#读文件
    fr=open(filename)
    dataSet=[];labelSet=[];countX={};tot=-1;zhuan={};pan={}
    for line in fr.readlines():
        curLine=line.strip().split(',')
        if ('Attrition' in line):
            o=-1
            for i in curLine:
                tot+=1;o+=1
                if(o==1):
                    tot-=1
                    continue
                if(tot==0):
                    countX[0]='Age'
                    zhuan['Age']=0
                else:
                    countX[tot]=i
                    zhuan[i]=tot
            continue
        fitLine=[];o=-1;j=-1;
        for i in curLine:
            o+=1;j+=1
            if(o==1):
                j-=1
                continue
            if(i.isdigit()):
                fitLine.append(float(i))
                pan[j]=0
            else:
                pan[j]=1
                if(i not in countX):
                    tot+=1
                    countX[i]=tot
                    zhuan[tot]=i
                fitLine.append(float(countX[i]))
        dataSet.append(fitLine)
        labelSet.append(curLine[1])
    return dataSet,labelSet,countX,zhuan,pan
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
def choosesplit(dataSet,labelSet,ops=(0.00001,3)):
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
        EntMu = calcShonnonEnt(bb)
        for i in nSet:
            if(i==max(nSet))or(i==min(nSet)):continue
            matA, matB, labA, labB=splitData(dataSet,labelSet,j,i)
            probA=float(len(labA)/len(labelSet));
            probB = float(len(labB) / len(labelSet));
            splitEnt=probA*calcShonnonEnt(labA)+probB*calcShonnonEnt(labB)
            if(splitEnt/EntMu<bestS):
                bestS=splitEnt/EntMu
                bestFeat=j
                bestValue=i
    if(bestS<ops[0]):
        return None,majority(labelSet)
    matA, matB, labA, labB = splitData(dataSet, labelSet, bestFeat, bestValue)
    if(shape(matA)[0]<ops[1])or(shape(matB)[0]<ops[1]):
        return None,majority(labelSet)
    return bestFeat,bestValue
def createTree(dataSet,labelSet,countX,zhuan,pan):
    feat,val=choosesplit(dataSet,labelSet)
    if(feat==None):
        return val
    TreeX = {}
    TreeX['feat']=countX[feat]
    if(pan[feat]==1):
        TreeX['val']=zhuan[int(val)]
    else:TreeX['val']=val
    matA, matB, labA, labB = splitData(dataSet, labelSet, feat, val)
    TreeX['left']=createTree(matA,labA,countX,zhuan,pan)
    TreeX['right'] = createTree(matB, labB,countX,zhuan,pan)
    return TreeX
def classify(dataX,TreeX):
    if('feat' not in TreeX):
        return TreeX
    feat=TreeX['feat'];val=TreeX['val']
    if(pan[zhuan[feat]]==1):
        val=countX[val]
    if(dataX[0,zhuan[feat]]<val):
        return classify(dataX,TreeX['left'])
    else:
        return classify(dataX,TreeX['right'])
if __name__=='__main__':
    dataSet,labelSet,countX,zhuan,pan=loadDataSet('联创有限公司裁员表.csv')
    dataSet=mat(dataSet);
    myTree=createTree(dataSet,labelSet,countX,zhuan,pan)
    print(myTree)
    error=0;fen=dataSet.shape[0]
    for i in range(len(labelSet)):
        u=classify(dataSet[i],myTree)
        if(u!=labelSet[i]):error+=1
    print(float(fen-error)/fen)
