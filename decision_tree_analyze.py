# -*- coding:utf-8 *-*
# @Time    : 2017/10/30 0030 20:46
# @Author  : LQY
# @File    : decision_tree_analyze.py
# @Software: PyCharm Community Edition
# from sklearn import tree
import pandas

from pandas import Series, DataFrame
from sklearn.datasets import load_iris
from sklearn import tree
import sys
import os
from IPython.display import Image
import pydotplus
import numpy
os.environ["PATH"] += os.pathsep + 'D:\Anaconda\Library\\bin\graphviz'
import graphviz
from IPython.display import Image

# iris = load_iris()
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(iris.data, iris.target)
# with open("iris.dot", 'w') as f:
#     f = tree.export_graphviz(clf, out_file=f)
# dot_data = tree.export_graphviz(clf, out_file=None,
#                                     feature_names=iris.feature_names,
#                                     class_names=iris.target_names,
#                                     filled=True, rounded=True,
#                                     special_characters=True)
# dot_data = tree.export_graphviz(clf, out_file=None)
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf("iris.pdf")
def visualization_tree():
    df = pandas.read_csv('E:\wash_data\\all_samples\\all_samples\\all_samples\\for_7model_all.csv')
    # #help(pandas.read_csv)
    df=df.fillna(0)
    Y=df['label']
    X=df.drop(['label'],axis=1)
    print X.columns
    clf = tree.DecisionTreeClassifier(max_depth=6)
    clf = clf.fit(X, Y)
    # with open("E:\wash_data\\all_samples\\all_samples\\all_samples\\7model_tree.dot", 'w') as f:
    #     f = tree.export_graphviz(clf, out_file=f)
    dot_data = tree.export_graphviz(clf, out_file=None,filled=True,
                                         feature_names=X.columns,
                                         class_names= {0:'liushi',1:'feiliushi'},
                                         rounded=True,
                                         special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("E:\wash_data\\all_samples\\all_samples\\all_samples\\7model_tree.pdf")
    #graph = pydotplus.graph_from_dot_data(dot_data)
    #Image(graph.create_png())
def cart_model():
    df = pandas.read_csv('E:\wash_data\generate_feature_28\\for_28model_train1.csv')
    df = df.fillna(0)
    # #help(pandas.read_csv)
    Y_train = df['label']
    X_train = df.drop(['label'], axis=1)
    #print X_train.columns
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, Y_train)
    test_data=pandas.read_csv('E:\wash_data\generate_feature_28\\for_28model_0117_test.csv')
    test_data=test_data.fillna(0)
    Y_test = test_data['label']
    X_test = test_data.drop(['label'],axis=1)
    p_right=0
    r_right=0
    neg_count=0
    #print X_test.shape[0]
    for i in range(X_test.shape[0]):
        #print Y_test[i]
        if Y_test[i]==0:
            neg_count+=1
        #print X_test.iloc[i,:]
        y_predict=clf.predict(X_test.iloc[i,:])
        if y_predict==Y_test[i]:
            p_right+=1
            if y_predict==0:
                r_right+=1
    precision = p_right/float(X_test.shape[0])
    recall = r_right/float(neg_count)
    print precision,recall
cart_model()
