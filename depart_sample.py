# -*- coding:utf-8 *-*
# @Time    : 2017/9/27 0027 14:25
# @Author  : LQY
# @File    : depart_sample.py
# @Software: PyCharm Community Edition
from numpy import *
import pandas as pd
def depart_samples():
    f=open('E:\wash_data\\all_samples\\for_28model_all.csv','r')
    fw1=open('E:\wash_data\\all_samples\\for_28model_positive.csv','w')
    fw2=open('E:\wash_data\\all_samples\\for_28model_negative.csv','w')
    for line in f.readlines():
        line1=line.split(',')
        if line1[0]=='1':
            fw1.write(line)
        else:
            fw2.write(line)


def dataDiscretize():
    dataSet = pd.read_csv('E:\wash_data\\all_samples\\for_7model_all.csv', header=0, delimiter=',')
    data = dataSet.drop(['label'], axis=1)
    #data.describe.to_csv('E:\wash_data\\all_samples\\for_7model_all_describe.csv', header=True, index=-1)
    column = data.columns
    m,n = shape(data)    #获取数据集行列（样本数和特征数)
    print m,n
    disMat = tile([0.00],shape(dataSet))  #初始化离散化数据集
    for i in range(n):    #由于最后一列为类别，因此遍历前n-1列，即遍历特征列
        # x = [l[i] for l in dataSet] #获取第i+1特征向量
        # y = pd.cut(x,3,labels=['low','middle','high'])   #调用cut函数，将特征离散化为10类，可根据自己需求更改离散化种类
        a=data.columns[i]
        # print data[a]
        y = pd.cut(data[a], 5,labels=[0,1,2,3,4])
        print a
        for k in range(n):  #将离散化值传入离散化数据集
            disMat[k][i] = y[k]
    df=pd.DataFrame(disMat)
    df.to_csv('E:\wash_data\\all_samples\\for_7model_all_lisan.csv', header=True, index=-1)
dataDiscretize()
