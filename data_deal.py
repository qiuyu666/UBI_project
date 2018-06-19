# -*- coding:utf-8 *-*
# @Time    : 2017/8/25 0025 14:38
# @Author  : LQY
# @File    : data_deal.py
# @Software: PyCharm Community Edition

import os
import math
from os.path import join, getsize
import pandas as pd
import numpy as np
from datetime import datetime


def user_reg_statistic():
    """
        统计每天注册人数
    """
    reg_data = {}   #存放注册统计信息，主键是日期，value是每天注册人数
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2015_01\gro_int\\int_user_registration','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[11] in reg_data.keys():
                reg_data[line[11]]+=1
            else:
                reg_data[line[11]]=1
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\\int_user_registration','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[11] in reg_data.keys():
                reg_data[line[11]]+=1
            else:
                reg_data[line[11]]=1
    dict = sorted(reg_data.items(), key=lambda d: d[0])  #排序，按主键日期对其进行排序,
    fw = open('E:\8-22_Ubi_data\data_deal\\reg_statistic_day.txt','w')
    for i in dict:
        fw.write(i[0]+'\t'+str(i[1])+'\n') #写入注册统计文件
    fw.close()

def achievement_static():
    cou=0
    with open('E:\wash_data\washfinal_2014_11.12\\1int_achievement_event','r') as f:
        for line in f.readlines():
            line = line.split('\t')
            if line[0] =='3886389':
                cou+=1
    print cou


#user_reg_statistic()
#achievement_static()
# raw_data=pd.read_table('E:\8-22_Ubi_data\data_deal\\reg_statistic_day.txt',header=-1,parse_dates=[0])
# print raw_data
# a = raw_data[1].astype(np.str)
# raw_data.pop(1)
# raw_data.insert(1,1,a)

#raw_data.insert()
#print raw_data
#print a

a=['1','2','3','4']
b=['5','6','7']
f=open('E:\\test','w')
for i in a:
    f.write(i+',')
f.write('\n')
for i in b:
    f.write(i+',')
f.write('\n')