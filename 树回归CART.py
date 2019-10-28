from numpy import *
import matplotlib.pyplot as plt
class treeNode():
    def __init__(self,feat,val,right,left):
        featureToSplitOn=feat
        valueOfSplit=val
        rightBranch=right
        leftBranch=left
def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split()
        fltLine=list(map(float,curLine))
        dataMat.append(fltLine)
    return dataMat
def binSplitDataSet(dataSet,feature,value):
    if(len(nonzero(dataSet[:,feature]>value)[0])>0):
        mat0=dataSet[nonzero(dataSet[:,feature]>value)[0],:]
    else: mat0=mat([])
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]
    return mat0,mat1
def regLeaf(dataSet):
    return mean(dataSet[:,-1])
def regErr(dataSet):
    return var(dataSet[:,-1])*shape(dataSet)[0]
def chooseBestSplit(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    tolS=ops[0];tolN=ops[1]
    if len(set(dataSet[:,-1].T.tolist()[0]))==1:
        return None,leafType(dataSet)
    m,n=shape(dataSet)
    S=errType(dataSet)
    bestS=inf;bestIndex=0;bestValue=0
    for featIndex in range(n-1):
        for splitVal in dataSet[:,featIndex].tolist():
            mat0,mat1=binSplitDataSet(dataSet,featIndex,splitVal)
            if(shape(mat0)[0]<tolN)or(shape(mat1)[0]<tolN):continue
            newS=errType(mat0)+errType(mat1)
            if newS<bestS:
                bestIndex=featIndex
                bestValue=splitVal
                bestS=newS
    if(S-bestS)<tolS:
        return None,leafType(dataSet)
    mat0,mat1=binSplitDataSet(dataSet,bestIndex,bestValue)
    if(shape(mat0)[0]<tolN)or(shape(mat1)[0]<tolN):
        return None,leafType(dataSet)
    return bestIndex,bestValue
global tot
def createTree(dataSet,leafType=regLeaf,errType=regErr,ops=(1,4)):
    feat,val=chooseBestSplit(dataSet,leafType,errType,ops)
    if feat==None:
        global tot
        tot+=1
        for i in range(dataSet.shape[0]):
            plt.plot(dataSet[i,0],dataSet[i,1],mark[tot])
        return val
    retTree={}
    retTree['spInd']=feat
    retTree['spVal']=val
    lSet,rSet=binSplitDataSet(dataSet,feat,val)
    retTree['left']=createTree(lSet,leafType,errType,ops)
    retTree['right']=createTree(rSet,leafType,errType,ops)
    return retTree
myDat=loadDataSet('data3.txt')
myMat=mat(myDat)
tot=1
mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
mark1=['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
mark=mark+mark1
print(createTree(myMat))
plt.show()