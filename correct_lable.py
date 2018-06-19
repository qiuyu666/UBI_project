# -*- coding:utf-8 *-*
# @Time    : 2017/9/14 0014 10:01
# @Author  : LQY
# @File    : correct_lable.py
# @Software: PyCharm Community Edition
from datetime import datetime
import pandas as pd
import numpy

def cor_lable():
    right_dic={}
    wrong_dic={}
    cor_label={}
    del_user={}
    flag=0
    f1=open('E:\8-22_Ubi_data\data_deal_new\\1101-1128\\user_for_28model_28','r')
    f2=open('E:\wash_data\generate_feature_28\\for_28model_1128.csv','r')
    for line in f1.readlines():
        line=line.strip().split('\t')
        right_dic[line[0]] =line[1]
        print line[0],line[1]
    for line in f2.readlines():
        if flag==1:
            line=line.split(',')
            wrong_dic[line[0]]=line[1]
            print line[0],line[1]
        flag = 1
    for key in wrong_dic:
        if key in right_dic:
            if wrong_dic[key] != right_dic[key]:
                cor_label[key]=right_dic[key]
        else:
            del_user[key]=wrong_dic[key]
    # f3=open('E:\wash_data\generate_feature_28\\for_28model_1128.csv','r')
    # f4=open('E:\wash_data\generate_feature_28\\for_28model_1128_new.csv','w')
    f3=pd.read_csv('E:\wash_data\generate_feature_28\\for_28model_1128.csv')
    for key in del_user:
        tem=int(f3[f3['id']==key].index.values)
        f3.drop(tem,inplace=True)
    for key in cor_label:
        f3.loc[f3['id'] == key,'label'] = cor_label[key]
    f3.to_csv('E:\wash_data\generate_feature_28\\for_28model_1128_new.csv',index=None)
cor_lable()


# f=pd.read_csv('E:\wash_data\\after_merge_feature_11\\for_14model_21.csv')
# a = int(f[f['id']==2065443].index.values)
# f.drop(a,inplace=True)
# f.to_csv('E:\wash_data\\after_merge_feature_11\\for_14model_211.csv',index=None)
# # a=f[f['id']==2065443]
# # a[id==2065443,'label']=0


