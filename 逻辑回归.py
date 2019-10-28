import numpy as np
import matplotlib
import matplotlib.pyplot as plt
def loadDataSet():
    dataMat=[]
    labelMat=[]
    fr=open('fan.in')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    fr.close()
    return dataMat,labelMat
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
def plotBestFit(weights,dataSet,labelSet):
    dataArr=np.array(dataSet)
    n=np.shape(dataSet)[0]
    xcord1=[];ycord1=[]
    xcord2=[];ycord2=[]
    for i in range(n):
        o=weights[0] + weights[1] * dataArr[i, 1] + weights[2] * dataArr[i, 2]
       # print(sigmoid(o), labelMat[i])
        if int(labelSet[i])==1:
            xcord1.append(dataArr[i,1])
            ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1])
            ycord2.append(dataArr[i,2])
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=20,c='red',marker='s',alpha=.5)
    ax.scatter(xcord2,ycord2,s=20,c='green',alpha=.5)
    x=np.arange(-3.0,3.0,0.1)
    y=(-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.title('DataSet')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
def classify(inX,weights):
    Cnt=0
    n=len(inX)
    x=inX[1]
    for i in range(n):
        Cnt+=weights[i]*inX[i]
    y = (-weights[0] - weights[1] * x) / weights[2]
    if(Cnt>0.0):return 1
    else: return 0
if __name__=='__main__':
    dataMat,labelMat=loadDataSet()
    fen = 20
    testSet = dataMat[-fen:]
    dataSet = dataMat[:-fen]
    testLabel = labelMat[-fen:]
    labelSet = labelMat[:-fen]
    weights=gradAscent(dataMat,labelMat)
    print(weights)
    plotBestFit(weights,dataSet,labelSet)
    error = 0
    for i in range(fen):
        label = classify(testSet[i], weights)
        if (label != testLabel[i]): error += 1
    print(float((fen - error) / fen))