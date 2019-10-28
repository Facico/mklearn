from numpy import *
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split(',')
        if ('?' in line): continue
        furLine=list(map(float,curLine[1:10]))
        dataSet.append(furLine)
        labelSet.append(int(curLine[-1:][0])-3)
    return dataSet,labelSet
def splitDataSet(dataSet,labelSet,prob=0.8):
    dataSetN=[];labelSetN=[]
    testSet=[];testLabel=[]
    n=len(dataSet)
    for i in range(n):
        o=random.random()
        if(o<prob):
            dataSetN.append(dataSet[i]);labelSetN.append(labelSet[i])
        else:
            testSet.append(dataSet[i]);testLabel.append(labelSet[i])
    return mat(dataSetN),labelSetN,mat(testSet),testLabel
def splitToRule(dataSet,labelSet,feat,val,o):
    n=dataSet.shape[0]
    error=mat(zeros((1,n)))
    if(o=='le'):
        for i in range(n):
            if(dataSet[i,feat]<=val):error[0,i]=(labelSet[i]==-1)
            else:error[0,i]=(labelSet[i]==1)
    else:
        for i in range(n):
            if(dataSet[i,feat]>val):error[0,i]=(labelSet[i]==-1)
            else:error[0,i]=(labelSet[i]==1)
    for i in range(n):
        if(error[0,i]==0):error[0,i]=-1
    return error
def buildStump(dataSet,labelSet,D):
    n,m=dataSet.shape
    errMin=inf;errorX=mat([])
    for feat in range(m):
        a=dataSet[:,feat].tolist()
        b=[i for item in a for i in item]
        b=set(b)
        for val in b:
            if(val==min(b)or(val==max(b))):continue
            for o in ['le','re']:
                errorX=splitToRule(dataSet,labelSet,feat,val,o)
                error=0
                for i in range(n):
                    if(errorX[0,i]!=labelSet[i]):error+=D[i,0]
                if(error<errMin):
                    errMin=error
                    classX={'feat':feat,'val':val,'o':o}
    return errMin,errorX,classX
def adaboostTrain(dataSet,labelSet,numX=20):
    n,m=dataSet.shape
    D=mat(ones((n,1))/n)
    classSet=[]
    classEnt=mat(zeros((n,1)))
    for i in range(numX):
        delta,errorX, stumpX=buildStump(dataSet,labelSet,D)
        alpha=float(0.5*(log((1-delta)/(max(delta,1e-16)))))
        stumpX['alpha']=alpha
        classSet.append(stumpX)
        for j in range(n):
            expX=1
            if(labelSet[j]!=errorX[0,j]):expX=-1
            D[j,0]*=exp(alpha*expX)
        D=D/D.sum()
        classEnt+=alpha*errorX.T
        sumx=0
        for j in range(n):
            if(labelSet[j]!=sign(classEnt[j,0])):sumx+=1
        if(sumx==0):break
    return classSet
def classify(testSet,testLabel,classSet):
    n=testSet.shape[0]
    m=len(classSet)
    classEnt=mat(zeros((n,1)))
    error=0
    for i in range(n):
        for j in range(m):
            errorX=splitToRule(testSet,testLabel,classSet[j]['feat'],classSet[j]['val'],classSet[j]['o'])
            classEnt+=classSet[j]['alpha']*errorX.T
    for j in range(n):
        if (testLabel[j]!= sign(classEnt[j, 0])): error+= 1
    return float((n-error)/n)
if __name__=='__main__':
    dataSetOld,labelSetOld=loadDataSet('breast-cancer-wisconsin.data')
    dataSet,labelSet,testSet,testLabel=splitDataSet(dataSetOld,labelSetOld)
    classSet=adaboostTrain(dataSet,labelSet)
    print(classify(testSet,testLabel,classSet))