import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import *
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split(',')
        if('?' in line):continue
        fitLine=list(map(float,curLine[1:10]))
        fitLine=[1]+fitLine
        dataSet.append(fitLine)
        labelSet.append((int(curLine[-1:][0])-2)/2)
    return dataSet,labelSet
def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))
def gradAscent(dataMatln,classLabels):
    dataMatrix=np.mat(dataMatln)
    labelMat=np.mat(classLabels).transpose()
    m,n=np.shape(dataMatrix)
    alpha=0.001
    maxCycles=500
    weights=np.ones((n,1))
    for k in range(maxCycles):
        h=sigmoid(dataMatrix*weights)
        error=labelMat-h
        weights=weights+alpha*dataMatrix.transpose()*error
    return weights.getA()
def sigmoid1(x):
    return 1.0/(1+exp(-x))
def classify(inX,weights):
    Cnt=0
    n=len(inX)
    for i in range(n):
        Cnt+=weights[i]*inX[i]
    Cnt=sigmoid1(Cnt)
    if(Cnt>0.5):return 1
    else: return 0
if __name__=='__main__':
    dataMat,labelMat=loadDataSet('breast-cancer-wisconsin.data')
    fen = 66
    testSet = dataMat[-fen:]
    dataSet = dataMat[:-fen]
    testLabel = labelMat[-fen:]
    labelSet = labelMat[:-fen]
    weights=gradAscent(dataMat,labelMat)
    print(len(weights))
    error=0
    for i in range(fen):
        label=classify(testSet[i],weights)
        if(label!=testLabel[i]):error+=1
    print(float((fen-error)/fen))