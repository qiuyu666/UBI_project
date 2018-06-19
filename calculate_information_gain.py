# -*- coding:utf-8 *-*
# @Time    : 2017/10/8 0008 10:53
# @Author  : LQY
# @File    : calculate_information_gain.py
# @Software: PyCharm Community Edition

from math import log
import operator
import numpy
import pandas

def calcShannonEnt(dataset):
    numEntries = len(dataset)
    labelcounts = {} #大括号为map
    for featVec in dataset:
        clabel = featVec[-1]   #取该数据样本的标签
        if clabel not in labelcounts.keys():
            labelcounts[clabel]=1
        labelcounts[clabel]+=1
    shannonEnt=0.0
    for key in labelcounts:
        prob = float(labelcounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt
#以上函数是求给定数据集的信息熵值



def splitDataSet(dataSet,axis,value):       #axis指的是第几个特征，value指的是数据集中第axis个特征值是value
    retDataSet = []                         #保证不修改dataSet
    for featVec in dataSet:
        if list(featVec)[axis] == value:          #求出第axis个特征，取值为value的子集
            reducedFeatVec = list(featVec)[:axis]        #取出axis前面的特征
            reducedFeatVec.extend(list(featVec)[axis+1:]) #取出axis后面的特征  相当于取出出去axis之外的所有特征
            retDataSet.append(reducedFeatVec)
    return retDataSet

def chooseBestFeatureToSplit(path):
    fw=open('E:\8-22_Ubi_data\dengpin\\discretize_28_info_gain.csv','w')
    dataset=pandas.read_csv(path,header=0,delimiter=',')
    print dataset
    column=dataset.columns

    print column
    data = pandas.read_csv(path, header=-1, delimiter=',')
    dataSet=numpy.array(data)
    iGList = {}
    print len(dataSet[0])
    numFeature = len(dataSet[0])-1   #得到第一个样本的特征个数
    print numFeature
    baseEntropy = calcShannonEnt(path)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeature):
        featList = [example[i] for example in dataSet] #把dataSet中的所有第i维特征值取出来
        uniqueVals = set(featList)  #将第i维特征值映射到集合上，得到特征值的不同取值
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))   #该子集占原数据集的比例
            newEntropy+=prob*calcShannonEnt(subDataSet)  #求按该特征分类后的信息熵
        infoGain = baseEntropy - newEntropy
        iGList[column[i]]=infoGain
        if(infoGain>bestInfoGain):  #求最大信息增益，并返回信息增益最大的分类特征
            bestInfoGain = infoGain
            bestFeature = column[i]
    print  bestFeature #信息增益最大的特征
    for key in iGList:
        fw.write(key+','+str(iGList[key])+'\n')

    #print iGList  #信息增益列表


#dataset = pandas.read_csv()
chooseBestFeatureToSplit(r'E:\8-22_Ubi_data\dengpin\\discretize_28.csv')
