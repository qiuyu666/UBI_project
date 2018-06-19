# -*- coding:utf-8 *-*
# @Time    : 2017/9/6 0006 15:05
# @Author  : LQY
# @File    : cancat_feature.py
# @Software: PyCharm Community Edition
import os
import pandas as pd
import xgboost
import numpy as np
from pandas import DataFrame


def compare_result():
    dic1={}
    dic2={}
    f=open('E:\wash_data\generate_feature_28\\for_28model_0109.csv','r')
    f1=open('E:\8-22_Ubi_data\data_deal_new\\1101-0109\user_for_28model_28','r')
    flag=0
    con=0
    con2=0
    for line in f.readlines():
        if flag==1:
            line=line.strip().split(',')
            dic1[line[0]] = line[1]
        flag=1

    for line in f1.readlines():
        line=line.strip().split('\t')
        dic2[line[0]]=line[1]
    # for key in dic1:
    #     if key in dic2:
    #         if dic2[key]!=dic1[key]:
    #             con+=1
    #             print key,dic2[key],dic1[key]
    #     else:
    #         print key,dic1[key]
    #         con2+=1
    #         #print key,dic2[key]
    for key in dic2:
        if key in dic1:
            if dic2[key]!=dic1[key]:
                con+=1
                print key,dic2[key],dic1[key]
        else:
            print key,dic2[key]
            con2+=1
                #print key,dic2[key]
    print con,con2
#compare_result()


def merge_featue():
    path = 'E:\wash_data\generate_feature_7_1107'
    paths=os.listdir(path)
    print paths
    a = pd.read_csv('E:\8-22_Ubi_data\data_deal_new\\1101-1107\\user_for_7model_07', header=None, delimiter='\t',names=['id','label'])#lable文件
    for p in paths:
        b=pd.read_csv(path+'\\'+p,header=0,delimiter=',')
        a =a.merge(b, how='left', on=['id'])
    a.to_csv('E:\wash_data\generate_feature_7\\for_7model_1107.csv',encoding = "utf-8",header=True,index=False)
#merge_featue()



#合并模型
def concact_feature():
    # j = pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1107.csv', header=0, delimiter=',')
    # i = pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1114.csv', header=0, delimiter=',')
    # h=pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1121.csv',header=0, delimiter=',')
    # a=pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1128.csv',header=0, delimiter=',')
    # b=pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1205.csv',header=0, delimiter=',')
    # c=pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1212.csv',header=0, delimiter=',')
    # d = pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1219.csv', header=0, delimiter=',')
    # e = pd.read_csv('E:\wash_data\generate_feature_7\\for_7model_1226.csv', header=0, delimiter=',')
    f = pd.read_csv('E:\wash_data\generate_feature_28\\for_28model_train.csv', header=0, delimiter=',')
    g = pd.read_csv('E:\wash_data\generate_feature_28\\for_28model_0117_test.csv', header=0, delimiter=',')
    # #d=pd.read_csv('E:\wash_data\\after_merge_feature\\7model\\for_7model_28.csv',header=0, delimiter=',')
    # list=[j,i,h,a,b,c,d,e,f,g]
    list = [f, g]
    # a = pd.read_csv('E:\wash_data\\after_merge_feature\\14model\\for_14model_14.csv', header=0, delimiter=',')
    # b = pd.read_csv('E:\wash_data\\after_merge_feature\\14model\\for_14model_21.csv', header=0, delimiter=',')
    # # c = pd.read_csv('E:\wash_data\\after_merge_feature\\14model\\for_14model_28.csv', header=0, delimiter=',')
    # list=[a,b]
    # a = pd.read_csv('E:\wash_data\\after_merge_feature\\21model\\for_21model_21.csv', header=0, delimiter=',')
    # b = pd.read_csv('E:\wash_data\\after_merge_feature\\21model\\for_21model_28.csv', header=0, delimiter=',')
    # list = [a, b]
    result=pd.concat(list)
    result.to_csv('E:\wash_data\generate_feature_28\\for_28model_all.csv',header=True,index=-1)
concact_feature()

#合并登录记录文件
def merge_login():
    fw=open('E:\wash_data\washfinal_2014_11.12\\1int_user_login', 'a')
    with open('E:\wash_data\washfinal_2015_01\\1int_user_login', 'r') as f:
        for line in f.readlines():
            fw.write(line)
















