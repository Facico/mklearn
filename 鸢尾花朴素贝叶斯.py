# -*- coding:utf-8 -*-
# 鸢尾花的特征作为数据
data = '''5.1,3.5,1.4,0.2,Iris-setosa
        4.9,3.0,1.4,0.2,Iris-setosa
        4.7,3.2,1.3,0.2,Iris-setosa
        4.6,3.1,1.5,0.2,Iris-setosa
        5.0,3.6,1.4,0.2,Iris-setosa
        5.4,3.9,1.7,0.4,Iris-setosa
        4.6,3.4,1.4,0.3,Iris-setosa
        5.0,3.4,1.5,0.2,Iris-setosa
        4.4,2.9,1.4,0.2,Iris-setosa
        4.9,3.1,1.5,0.1,Iris-setosa
        5.4,3.7,1.5,0.2,Iris-setosa
        4.8,3.4,1.6,0.2,Iris-setosa
        4.8,3.0,1.4,0.1,Iris-setosa
        4.3,3.0,1.1,0.1,Iris-setosa
        5.8,4.0,1.2,0.2,Iris-setosa
        5.7,4.4,1.5,0.4,Iris-setosa
        5.4,3.9,1.3,0.4,Iris-setosa
        5.1,3.5,1.4,0.3,Iris-setosa
        5.7,3.8,1.7,0.3,Iris-setosa
        5.1,3.8,1.5,0.3,Iris-setosa
        5.4,3.4,1.7,0.2,Iris-setosa
        5.1,3.7,1.5,0.4,Iris-setosa
        4.6,3.6,1.0,0.2,Iris-setosa
        5.1,3.3,1.7,0.5,Iris-setosa
        4.8,3.4,1.9,0.2,Iris-setosa
        5.0,3.0,1.6,0.2,Iris-setosa
        5.0,3.4,1.6,0.4,Iris-setosa
        5.2,3.5,1.5,0.2,Iris-setosa
        5.2,3.4,1.4,0.2,Iris-setosa
        4.7,3.2,1.6,0.2,Iris-setosa
        4.8,3.1,1.6,0.2,Iris-setosa
        5.4,3.4,1.5,0.4,Iris-setosa
        5.2,4.1,1.5,0.1,Iris-setosa
        5.5,4.2,1.4,0.2,Iris-setosa
        4.9,3.1,1.5,0.1,Iris-setosa
        5.0,3.2,1.2,0.2,Iris-setosa
        5.5,3.5,1.3,0.2,Iris-setosa
        4.9,3.1,1.5,0.1,Iris-setosa
        4.4,3.0,1.3,0.2,Iris-setosa
        5.1,3.4,1.5,0.2,Iris-setosa
        5.0,3.5,1.3,0.3,Iris-setosa
        4.5,2.3,1.3,0.3,Iris-setosa
        4.4,3.2,1.3,0.2,Iris-setosa
        5.0,3.5,1.6,0.6,Iris-setosa
        5.1,3.8,1.9,0.4,Iris-setosa
        4.8,3.0,1.4,0.3,Iris-setosa
        5.1,3.8,1.6,0.2,Iris-setosa
        4.6,3.2,1.4,0.2,Iris-setosa
        5.3,3.7,1.5,0.2,Iris-setosa
        5.0,3.3,1.4,0.2,Iris-setosa
        7.0,3.2,4.7,1.4,Iris-versicolor
        6.4,3.2,4.5,1.5,Iris-versicolor
        6.9,3.1,4.9,1.5,Iris-versicolor
        5.5,2.3,4.0,1.3,Iris-versicolor
        6.5,2.8,4.6,1.5,Iris-versicolor
        5.7,2.8,4.5,1.3,Iris-versicolor
        6.3,3.3,4.7,1.6,Iris-versicolor
        4.9,2.4,3.3,1.0,Iris-versicolor
        6.6,2.9,4.6,1.3,Iris-versicolor
        5.2,2.7,3.9,1.4,Iris-versicolor
        5.0,2.0,3.5,1.0,Iris-versicolor
        5.9,3.0,4.2,1.5,Iris-versicolor
        6.0,2.2,4.0,1.0,Iris-versicolor
        6.1,2.9,4.7,1.4,Iris-versicolor
        5.6,2.9,3.6,1.3,Iris-versicolor
        6.7,3.1,4.4,1.4,Iris-versicolor
        5.6,3.0,4.5,1.5,Iris-versicolor
        5.8,2.7,4.1,1.0,Iris-versicolor
        6.2,2.2,4.5,1.5,Iris-versicolor
        5.6,2.5,3.9,1.1,Iris-versicolor
        5.9,3.2,4.8,1.8,Iris-versicolor
        6.1,2.8,4.0,1.3,Iris-versicolor
        6.3,2.5,4.9,1.5,Iris-versicolor
        6.1,2.8,4.7,1.2,Iris-versicolor
        6.4,2.9,4.3,1.3,Iris-versicolor
        6.6,3.0,4.4,1.4,Iris-versicolor
        6.8,2.8,4.8,1.4,Iris-versicolor
        6.7,3.0,5.0,1.7,Iris-versicolor
        6.0,2.9,4.5,1.5,Iris-versicolor
        5.7,2.6,3.5,1.0,Iris-versicolor
        5.5,2.4,3.8,1.1,Iris-versicolor
        5.5,2.4,3.7,1.0,Iris-versicolor
        5.8,2.7,3.9,1.2,Iris-versicolor
        6.0,2.7,5.1,1.6,Iris-versicolor
        5.4,3.0,4.5,1.5,Iris-versicolor
        6.0,3.4,4.5,1.6,Iris-versicolor
        6.7,3.1,4.7,1.5,Iris-versicolor
        6.3,2.3,4.4,1.3,Iris-versicolor
        5.6,3.0,4.1,1.3,Iris-versicolor
        5.5,2.5,4.0,1.3,Iris-versicolor
        5.5,2.6,4.4,1.2,Iris-versicolor
        6.1,3.0,4.6,1.4,Iris-versicolor
        5.8,2.6,4.0,1.2,Iris-versicolor
        5.0,2.3,3.3,1.0,Iris-versicolor
        5.6,2.7,4.2,1.3,Iris-versicolor
        5.7,3.0,4.2,1.2,Iris-versicolor
        5.7,2.9,4.2,1.3,Iris-versicolor
        6.2,2.9,4.3,1.3,Iris-versicolor
        5.1,2.5,3.0,1.1,Iris-versicolor
        5.7,2.8,4.1,1.3,Iris-versicolor
        6.3,3.3,6.0,2.5,Iris-virginica
        5.8,2.7,5.1,1.9,Iris-virginica
        7.1,3.0,5.9,2.1,Iris-virginica
        6.3,2.9,5.6,1.8,Iris-virginica
        6.5,3.0,5.8,2.2,Iris-virginica
        7.6,3.0,6.6,2.1,Iris-virginica
        4.9,2.5,4.5,1.7,Iris-virginica
        7.3,2.9,6.3,1.8,Iris-virginica
        6.7,2.5,5.8,1.8,Iris-virginica
        7.2,3.6,6.1,2.5,Iris-virginica
        6.5,3.2,5.1,2.0,Iris-virginica
        6.4,2.7,5.3,1.9,Iris-virginica
        6.8,3.0,5.5,2.1,Iris-virginica
        5.7,2.5,5.0,2.0,Iris-virginica
        5.8,2.8,5.1,2.4,Iris-virginica
        6.4,3.2,5.3,2.3,Iris-virginica
        6.5,3.0,5.5,1.8,Iris-virginica
        7.7,3.8,6.7,2.2,Iris-virginica
        7.7,2.6,6.9,2.3,Iris-virginica
        6.0,2.2,5.0,1.5,Iris-virginica
        6.9,3.2,5.7,2.3,Iris-virginica
        5.6,2.8,4.9,2.0,Iris-virginica
        7.7,2.8,6.7,2.0,Iris-virginica
        6.3,2.7,4.9,1.8,Iris-virginica
        6.7,3.3,5.7,2.1,Iris-virginica
        7.2,3.2,6.0,1.8,Iris-virginica
        6.2,2.8,4.8,1.8,Iris-virginica
        6.1,3.0,4.9,1.8,Iris-virginica
        6.4,2.8,5.6,2.1,Iris-virginica
        7.2,3.0,5.8,1.6,Iris-virginica
        7.4,2.8,6.1,1.9,Iris-virginica
        7.9,3.8,6.4,2.0,Iris-virginica
        6.4,2.8,5.6,2.2,Iris-virginica
        6.3,2.8,5.1,1.5,Iris-virginica
        6.1,2.6,5.6,1.4,Iris-virginica
        7.7,3.0,6.1,2.3,Iris-virginica
        6.3,3.4,5.6,2.4,Iris-virginica
        6.4,3.1,5.5,1.8,Iris-virginica
        6.0,3.0,4.8,1.8,Iris-virginica
        6.9,3.1,5.4,2.1,Iris-virginica
        6.7,3.1,5.6,2.4,Iris-virginica
        6.9,3.1,5.1,2.3,Iris-virginica
        5.8,2.7,5.1,1.9,Iris-virginica
        6.8,3.2,5.9,2.3,Iris-virginica
        6.7,3.3,5.7,2.5,Iris-virginica
        6.7,3.0,5.2,2.3,Iris-virginica
        6.3,2.5,5.0,1.9,Iris-virginica
        6.5,3.0,5.2,2.0,Iris-virginica
        6.2,3.4,5.4,2.3,Iris-virginica
        5.9,3.0,5.1,1.8,Iris-virginica'''

import numpy as np

# 数据处理,取得150条的数据,将类别转化为1.0，2.0，3.0数字，因为后面使用NUMPY计算比较快，在类别的类型上和属性一样使用浮点型
data = data.replace(' ', '').replace("Iris-setosa", "1.0").replace("Iris-versicolor", "2.0").replace("Iris-virginica",
                                                                                                     "3.0").split('\n')
data = list(filter(lambda x: len(x) > 0, data))
data = [x.split(',') for x in data]
data = np.array(data).astype(np.float16)


# 将数据随机分成训练集与测试集
def splitData(trainPrecent=0.7):
    train = []
    test = []
    for i in data:
        (train if np.random.random() < trainPrecent else test).append(i)
    return np.array(train), np.array(test)


trainData, testData = splitData()
print("共有%d条数据，分解为%d条训练集与%d条测试集" % (len(data), len(trainData), len(testData)))
clf = set(trainData[:, -1])  # 读取每行最后一个数据，用set得出共有几种分类,本例为1.0,2.0,3.0
trainClfData = {}  # 有于存储每个类别的均值与标准差
prob={}
for x in clf:
    clfItems = np.array(list(filter(lambda i: i[-1] == x, trainData)))[:, :-1]  # 从训练集中按类别过滤出记录
    prob[x]=float(len(clfItems)/len(trainData))
    mean = clfItems.mean(axis=0)  # 计算每个属性的平均值
    stdev = np.sqrt(np.sum((clfItems - mean) ** 2, axis=0) / float(len(clfItems) - 1))  # 计算每个属性的标准差
    trainClfData[x] = np.array([mean, stdev]).T  # 对每个类形成固定的数据格式[[属性1均值，属性1标准差],[属性2均值,属性2标准差]]
# print(trainClfData)
result = []
for testItem in testData:
    itemData = testItem[0:-1]  # 得到训练的属性数据
    itemClf = testItem[-1]  # 得到训练的分类数据

    prediction = {}  # 用于存储单条记录集对应的每个类别的概率
    for clfItem in trainClfData:
        # 测试集中单条记录的每个属性在与训练集中进行比对应用的朴素贝叶斯算法，
        probabilities = np.exp(
            -1 * (testItem[0:-1] - trainClfData[clfItem][:, 0]) ** 2 / (trainClfData[clfItem][:, 1] ** 2 * 2)) / (
                                    np.sqrt(2 * np.pi) * trainClfData[clfItem][:, 1])
        # 将每个属性的概率相乘，等到最终该类别的概率
        clfPrediction = 1
        for proItem in probabilities:
            clfPrediction *= proItem
        prediction[clfItem] = clfPrediction*prob[clfItem]
    # 取得最大概率的那个类别
    maxProbablity = None
    for x in prediction:
        if maxProbablity == None or prediction[x] > prediction[maxProbablity]:
            maxProbablity = x

    # 将计算的数据返回，后面有一句print我关闭了，打开就可以看到这些结果
    result.append({'数据': itemData.tolist()
                      , '实际分类': itemClf
                      , '各类别概率': prediction
                      , '测试分类(最大概率类别)': maxProbablity
                      , '是否正确': 1 if itemClf == maxProbablity else 0})
rightCount = 0;
for x in result:
    rightCount += x['是否正确']
    # print(x) #打印出每条测试集计算的数据
print('共%d条测试数据，测试正确%d条,正确率%2f:' % (len(result), rightCount, rightCount / len(result)))