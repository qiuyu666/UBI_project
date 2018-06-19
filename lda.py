# -*- coding:utf-8 *-*
# @Time    : 2017/10/29 0029 19:12
# @Author  : LQY
# @File    : lda.py
# @Software: PyCharm Community Edition

from sklearn.lda import LDA
import pandas
from pandas import Series, DataFrame

df = pandas.read_csv('E:\8-22_Ubi_data\data_analyze\kills_deaths\\for_28model_mean_kills_deaths.csv',header=None)
#help(pandas.read_csv)
df=df.fillna(0)
# print df
# print df[0]
y=df[0]
X=df.drop([0],axis=1)
print y
print X

#X = iris.data[:-5]
#pre_x = iris.data[-5:]
#y = iris.target[:-5]
#print ('first 10 raw samples:', X[:10])
clf = LDA()
clf.fit(X, y)
X_r = clf.transform(X)
X_r=DataFrame(X_r)
#pre_y = clf.predict(pre_x)
#降维结果
X_r.to_csv('E:\8-22_Ubi_data\data_analyze\kills_deaths\\for_28model_mean_kills_deaths_lda.csv')
#print ('first 10 transformed samples:', X_r[:10])
#预测目标分类结果
#print ('predict value:', pre_y)