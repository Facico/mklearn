from numpy import *
def loadDataSet(filename):
    fr=open(filename)
    dataSet=[];labelSet=[]
    for line in fr.readlines():
        curLine=line.strip().split(',')
        if ('?' in line): continue
        furLine=list(map(float,curLine[1:10]))
        dataSet.append(furLine)
        labelSet.append(curLine[-1:][0])
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
    return array(dataSetN),labelSetN,array(testSet),testLabel
def calcDataValue(dataSet,labelSet):
    labelVal={};prob={}
    SetX=set(labelSet)
    for i in SetX:
        labelji=[]
        for j in range(dataSet.shape[0]):
            if(labelSet[j]==i):labelji.append(dataSet[j].tolist())
        labelji=array(labelji)
        prob[i]=float(len(labelji)/len(dataSet))
        mean=labelji.mean(axis=0)
        biao=sqrt(sum((labelji-mean)**2,axis=0)/(len(labelji)-1))
        labelVal[i]=array([mean,biao]).T
    return SetX,labelVal,prob
def classify(labelVal,prob,testSet,testLabel,SetX):
    error=0;n=len(testSet)
    for i in range(n):
        maxx=0;xuan=0
        for item in SetX:
            probLabel=exp(-1*(testSet[i]-labelVal[item][:,0])**2/(labelVal[item][:,1]**2 *2))/(
                    sqrt(2*pi)*labelVal[item][:,1])
            gailv=prob[item]
            for j in probLabel:gailv*=j
            if(gailv>maxx):
                maxx=gailv
                xuan=item
        if(xuan!=testLabel[i]):error+=1
    return float((n-error)/n)
if __name__=='__main__':
    dataSetO,labelSetO=loadDataSet('breast-cancer-wisconsin.data')
    dataSet, labelSet, testSet, testLabel=splitDataSet(dataSetO,labelSetO)
    SetX,labelVal,prob=calcDataValue(dataSet,labelSet)
    print(classify(labelVal,prob,testSet,testLabel,SetX))