from pandas import *
from numpy import *
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
if __name__=='__main__':
    names=['Age','Attrition','BusinessTravel','DailyRate','Department','DistanceFromHome','Education',
           'EducationField','EmployeeCount','EmployeeNumber','EnvironmentSatisfaction','Gender',
           'HourlyRate','JobInvolvement','JobLevel','JobRole','JobSatisfaction','MaritalStatus',
           'MonthlyIncome','MonthlyRate','NumCompaniesWorked','OverTime','PercentSalaryHike',
           'PerformanceRating','RelationshipSatisfaction','StockOptionLevel','TotalWorkingYears',
           'TrainingTimesLastYear','WorkLifeBalance','YearsAtCompany','YearsInCurrentRole',
           'YearsSinceLastPromotion','YearsWithCurrManager']
    fr = read_csv("联创有限公司裁员表.csv", header=None, names=names)

    datas = fr.replace("?", nan).dropna(how='any')
    datas = datas.drop(0, axis=0)
    #上面为处理缺失值
    n = len(datas['Age'])#表示文件纵长
    m = 33#表示文件横长
    countX = {}#给离散值标为连续值的字典
    tot = 0#给离散值标为连续值的变量
    for i in range(n):
        for j in range(m):
            x=datas.iloc[i,j]
            if(x.isdigit()==0):#判断是否为离散值
                if (x not in countX):
                    tot += 1
                    countX[x] = tot
                datas.iloc[i,j]=countX[x]
            else:
                datas.iloc[i,j]=int(datas.iloc[i,j])

    X = datas[[names[0]] + names[2:35]]#特征
    Y = datas[names[1]]#标签
    dataSet, testSet, labelSet, testLabel = train_test_split(X, Y, test_size=0.1, random_state=0)
    #上面为分裂数据
    ss = StandardScaler()
    dataSet = ss.fit_transform(dataSet)
    #上面为标准化处理
    logicX = LogisticRegression()
    logicX.fit(dataSet, labelSet)
    pred = logicX.predict(testSet)
    print(logicX.score(testSet, testLabel))#预测准确率
    print(metrics.classification_report(testLabel, pred))#输出包括召回率等的表格
