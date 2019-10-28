from numpy import *
import operator
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        try:
            curLine=line.strip().split(',')
            fitLine=list(map(float,curLine[:4]))
            dataSet.append(fitLine)
            labelSet.append(curLine[-1:][0])
        except ValueError:
            ans=1
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
    return (20.0-error)/20.0
if __name__=='__main__':
    dataSet,labelSet=loadDataSet('iris.data')
    dataSet=array(dataSet)
    dataSetN=dataProduce(dataSet)
    testSet=dataSetN[-20:];dataSet=dataSetN[:-20]
    testLabel = labelSet[-20:];labelSet = labelSet[:-20]
    maxx=0.0
    for K in range(1,21):
        maxx=max(classify(K),maxx)
    print(maxx)
    """mark=['ob','or','ok','rb']
    classN={};tot=-1
    fig=plt.figure()
    ax=fig.gca(projection='3d')
    for i in range(100):
        if(labelSet[i] not in classN):
            tot+=1
            classN[labelSet[i]]=tot
        mm=mark[classN[labelSet[i]]]
        ax.scatter3D(dataSet[i,0],dataSet[i,1],dataSet[i,2],'ob')
    plt.show()"""