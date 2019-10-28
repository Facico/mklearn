import numpy as np
import struct
from numpy import *
import operator
def decode_idx3_ubyte(idx3_ubyte_file):
    bin_data = open(idx3_ubyte_file, 'rb').read()
    offset = 0
    fmt_header = '>iiii'
    magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
    image_size = num_rows * num_cols
    offset += struct.calcsize(fmt_header)
    fmt_image = '>' + str(image_size) + 'B'
    images = np.empty((num_images, num_rows, num_cols))
    for i in range(num_images):
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
        offset += struct.calcsize(fmt_image)
    return images
def decode_idx1_ubyte(idx1_ubyte_file):
    bin_data = open(idx1_ubyte_file, 'rb').read()
    offset = 0
    fmt_header = '>ii'
    magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)
    offset += struct.calcsize(fmt_header)
    fmt_image = '>B'
    labels = np.empty(num_images)
    for i in range(num_images):
        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
        offset += struct.calcsize(fmt_image)
    return labels
def loadDataSet():
    dataSet= decode_idx3_ubyte('train-images.idx3-ubyte')
    labelSet = decode_idx1_ubyte('train-labels.idx1-ubyte')
    return dataSet,labelSet
def loadDataSet1():
    dataSet= decode_idx3_ubyte('t10k-images.idx3-ubyte')
    labelSet = decode_idx1_ubyte('t10k-labels.idx1-ubyte')
    return dataSet,labelSet
def dataProduce(dataSet,labelSet,x):
    sum,m,n=dataSet.shape
    dataSetN=[];labelSetN=[]
    countN={0.0:0,3.0:0,6.0:0,
            1.0:0,4.0:0,7.0:0,
            2.0:0,5.0:0,8.0:0,9.0:0,}
    for i in range(sum):
        if(countN[labelSet[i]]>=x):continue
        countN[labelSet[i]]+=1
        labelSetN.append(labelSet[i])
        a=[i for item in dataSet[i] for i in item]
        dataSetN.append(a)
    dataSetN=array(dataSetN)
    return dataSetN,labelSetN
def datagao(dataSet):
    m,n=dataSet.shape
    dataSetN=dataSet.copy()
    for j in range(n):
        minx=min(dataSet[:,j])
        maxx=max(dataSet[:,j])
        if(minx==maxx):maxx=minx+1
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
    return (nn-error)/nn
if __name__=='__main__':
    X,Y,K=400,20,20
    dataSetOld,labelSetOld=loadDataSet()
    dataSetN,labelSet=dataProduce(dataSetOld,labelSetOld,X)
    dataSet=datagao(dataSetN)
    testSetOld, testLabelOld = loadDataSet1()
    testSetN ,testLabel= dataProduce(testSetOld,testLabelOld,Y)
    testSet=datagao(testSetN)
    """maxx=0.0
    for k in range(1,50):
        maxx=max(classify(k),maxx)"""
    trueProd=classify(K)
    print(trueProd)
    #print(maxx)