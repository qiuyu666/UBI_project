# -*- coding:utf-8 *-*
# @Time    : 2017/9/10 0010 19:04
# @Author  : LQY
# @File    : gbdt.py
# @Software: PyCharm Community Edition
import numpy
import pandas
import xgboost as xg
import matplotlib.pylab as plt
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
#from tpot import TPOTClassifier
#from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn import tree
from sklearn import ensemble
from sklearn import linear_model
from sklearn import svm
import dimReduction


def load_data(path):

    df = pandas.read_csv(path)
    label = df.label
    data = df.drop(['label'], axis=1)
    # data=data.fillna(0) #空值处补0
    # #data=data.fillna(data.mean())#空值处填充均值
    # data=dimReduction.dimReduction(data) #降维+归一化

    return (data, label)

def xgb(train, test,path):

    X_train, X_val, y_train, y_val = train_test_split (train[0], train[1], train_size=0.8,random_state=0)

    dtrain = xg.DMatrix(X_train, y_train)
    dval = xg.DMatrix(X_val, y_val)
    dtest = xg.DMatrix(test)

    params = {}
    params["booster"] = "gbtree"
    # params["objective"] = "reg:linear"  # 线性回归
    params["objective"] = "binary:logistic"  # 逻辑回归
    params["eta"] = 0.01  # 0.1
    params["gamma"] = 0.1  # 树的叶子节点上作进一步分区所需的最小损失减少,越大越保守，一般0.1、0.2这样子
    params["max_depth"] = 3  # 默认为6 # 构建树的深度，越大越容易过拟合
    params["min_child_weight"] = 3  # 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
    # #这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting
    params["silent"] = 1  # 设置成1则没有运行信息输出，最好是设置为0
    params['alpha'] = 0.1  # L1 正则项参数
    # params['lambda'] = 2  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合
    params['eval_metric '] = 'logloss'
    num_round = 100

    watchlist = [(dtrain, 'train'), (dval, 'val')]
    plst = list (params.items ())  # Using 5000 rows for early stopping.
    print ("训练开始\n")

    bst = xg.train (plst, dtrain, num_boost_round=num_round, evals=watchlist, early_stopping_rounds=30)
    bst.dump_model(path+'\\dump.raw_28.txt')
    #bst.dump_model('dump.raw.txt', 'featmap.txt')
    limit = bst.best_iteration
    y_pred = bst.predict(dtest, ntree_limit=limit)
    feat_imp = pandas.Series(bst.get_fscore()).sort_values(ascending=False)
    feat_imp.to_csv(path+'\\feature_importance-21.csv')  # 特征重要性文件
    feat_imp.plot(kind='bar', title='Feature Importances')
    plt.ylabel('Feature Importance Score')
    plt.show()
    # bst.dump_model('dump.raw.txt')
    # bst.dump_model('dump.raw.txt','featmap.txt')


    return y_pred


def run_xgb():
    train = load_data('E:\wash_data\generate_feature_21\\for_21model_train.csv')
    test = load_data('E:\wash_data\generate_feature_21\\for_21model_0117_test.csv')
    # train = load_data (r'E:\育碧\data\9-6data_with_null\nov.csv')
    # test = load_data (r'E:\育碧\data\9-6data_with_null\dec.csv')
    print(train[0].columns)

    y_pred = xgb(train=train, test=test[0],path='E:\wash_data\generate_feature_21')

    df = pandas.DataFrame(y_pred)
    df.to_csv('E:\wash_data\generate_feature_21\pred-21csv', header=None, index=None)
    print(y_pred.shape)
    for i in range(len(y_pred)):
        y_pred[i] = 1 if y_pred[i] > 0.5 else 0
    #print(metrics.classification_report(test[1], y_pred))

    print metrics.precision_score(test[1], y_pred)  # 准确率 输出：1.0
    print metrics.recall_score(test[1], y_pred)  # 召回率 输出： 0.5
    print metrics.f1_score(test[1], y_pred)  # f1分数 输出：0.66
    fpr, tpr, thresholds = metrics.roc_curve(test[1], y_pred, pos_label=2)
    print fpr  # 输出：[ 0.   0.5  0.5  1. ]
    print tpr  # 输出：[ 0.5  0.5  1.   1. ]
    print thresholds  # 输出：[ 0.8   0.4   0.35  0.1 ]
    print metrics.roc_auc_score(test[1], y_pred)
run_xgb()


def LR_classifier():
    train = load_data(r'C:\Users\Administrator\Desktop\UBI\7\training-7.csv')
    test = load_data(r'C:\Users\Administrator\Desktop\UBI\7\test-7.csv')
    classifier = LogisticRegression()  # 使用类，参数全是默认的
    classifier.fit(train[0], train[1])  # 训练数据来学习，不需要返回值
    x = classifier.predict(test[0])  # 测试数据，分类返回标记


    print x


def get_model_effitc():
    train = load_data(r'C:\Users\Administrator\Desktop\UBI\7\training-7.csv')
    test = load_data(r'C:\Users\Administrator\Desktop\UBI\7\test-7.csv')
    lr = linear_model.LogisticRegression()
    lr_scores = cross_validation.cross_val_score(lr, train[0], train[1], cv=5)
    print("logistic regression accuracy:")
    print(lr_scores)

    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=8, min_samples_split=5)
    clf_scores = cross_validation.cross_val_score(clf, train[0], train[1], cv=5)
    print("decision tree accuracy:")
    print(clf_scores)

    rfc = ensemble.RandomForestClassifier(criterion='entropy', n_estimators=3, max_features=0.5, min_samples_split=5)
    rfc_scores = cross_validation.cross_val_score(rfc, train[0], train[1])
    print(rfc_scores)

    etc = ensemble.ExtraTreesClassifier(criterion='entropy', n_estimators=3, max_features=0.6, min_samples_split=5)
    etc_scores = cross_validation.cross_val_score(etc, train[0], train[1], cv=5)
    print("extra trees accuracy:")
    print(etc_scores)

    gbc = ensemble.GradientBoostingClassifier()
    gbc_scores = cross_validation.cross_val_score(gbc, train[0], train[1], cv=5)
    print("gradient boosting accuracy:")
    print(gbc_scores)
#get_model_effitc()

