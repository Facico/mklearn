from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split()
        if('?' in line):continue
        fitLine=list(map(float,curLine))
        dataSet.append(fitLine)
     #   labelSet.append(curLine[-1:][0])
    return dataSet
def binSplitDataSet(dataSet,feature,value):
    mat0=dataSet[nonzero(dataSet[:,feature]>value)[0],:]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]
    return mat0,mat1
def regLeaf(dataSet):
    """a=dataSet[:,-1].tolist()
    return median(a)"""
    a=dataSet[:,-1].tolist()
    c=[i for item in a for i in item]
    a=list(map(int,c))
    b=bincount(a)
    return argmax(b)
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
        a=dataSet[:,featIndex].tolist()
        b=[i for item in a for i in item]
        SetX=set(b)
        for splitVal in SetX:
            if(splitVal==min(SetX))or(splitVal==max(SetX)):continue
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
    retTree = {}
    if feat==None:
        retTree['spVal']=val
        return retTree
    retTree['spInd']=feat
    retTree['spVal']=val
    lSet,rSet=binSplitDataSet(dataSet,feat,val)
    try:
        retTree['left']=createTree(lSet,leafType,errType,ops)
    except TypeError:
        ans=1
    retTree['right']=createTree(rSet,leafType,errType,ops)
    return retTree
def classify(dataX,TreeX):
    if('spInd' not in TreeX):
        return TreeX['spVal']
    feat=TreeX['spInd'];val=TreeX['spVal']
    if(dataX[0,feat]<val):
        return classify(dataX,TreeX['left'])
    else:
        return classify(dataX,TreeX['right'])
if __name__=='__main__':
    myDat=loadDataSet('abalone.txt')
    myMat=mat(myDat)
    fen = 2000
    testSet = myMat[-fen:];
    dataSet = myMat[:-fen]
  #  testLabel = myLabel[-fen:];
   # labelSet = myLabel[:-fen]
    myTree=createTree(dataSet)
   # print(myTree)
    pan=2
    error=0
    for i in range(fen):
        u = float(classify(testSet[i], myTree))
        if (abs(u-testSet[i,-1])>pan): error += 1
    print(float((fen-error)/fen))