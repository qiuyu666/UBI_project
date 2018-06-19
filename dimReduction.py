# -*- coding: utf-8 -*-
"""
@author: shun
"""
import pandas as pd
import numpy as np

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

basePath=""
################################## 参数说明 ###########################
# 函数原型：sklearn.decomposition.PCA(n_components=None, copy=True, whiten=False)
# n_components:
#           意义：PCA算法中所要保留的主成分个数n，也即保留下来的特征个数n
#            类型：int 或者 string，缺省时默认为None，所有成分被保留。
#           赋值为int，比如n_components=1，将把原始数据降到一个维度。
#           赋值为string，比如n_components='mle'，将自动选取特征个数n，使得满足所要求的方差百分比。
# copy:类型：bool，True或者False，缺省时默认为True。
#       意义：表示是否在运行算法时，将原始训练数据复制一份。若为True，则运行PCA算法后，原始训练数据的值不            会有任何改变，因为是在原始数据的副本上进行运算；若为False，则运行PCA算法后，原始训练数据的              值会改，因为是在原始数据上进行降维计算。
# whiten:
#       类型：bool，缺省时默认为False
#       意义：白化，使得每个特征具有相同的方差。
################################## 参数说明 ###########################


def  dimReduction(data,isStandard=True,method="PCA"):
    """

    :param data: 数据输入dataframe
    :param isStandard:是否进行归一化
    :param method 方法列表："PCA" "TSNE"
    :return:返回降维结果
    """
    print()
    if isStandard==True:
        scaler = preprocessing.StandardScaler()
        scale_X = scaler.fit_transform(data) # 归一化
    else :
        scale_X=data
    if method=="TSNE":
        model=TSNE(n_components="mle")
    else:
        model = PCA(n_components="mle",svd_solver='full',copy=False)
    newdata=model.fit_transform(scale_X)
    return newdata

def main():
    data=([[1., 1.],
       [0.9, 0.95],
       [1.01, 1.03],
       [2., 2.],
       [2.03, 2.06],
       [1.98, 1.89],
       [3., 3.],
       [3.03, 3.05],
       [2.89, 3.1],
       [4., 4.],
       [4.06, 4.02],
       [3.97, 4.01]])
    data=pd.DataFrame(data)
    newdata=dimReduction(data)

print()

if __name__ == "__main__":
    main()