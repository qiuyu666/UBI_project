# -*- coding:utf-8 *-*
# @Time    : 2017/8/25 0025 15:28
# @Author  : LQY
# @File    : data_display.py
# @Software: PyCharm Community Edition
from __future__ import division
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']


def reg_statistic_dis():
    data=[]
    num_of_users=[]
    f= open('E:\8-22_Ubi_data\data_deal\\reg_statistic_day.txt','r')
    for line in f.readlines():
        line= line.split('\t')
        data.append(line[0])
        num_of_users.append(int(line[1]))
    x = range(len(data))
    plt.title(u'每天玩家注册情况')  # 图标名称
    #label = [u"流失", u"非流失"]  # 标注
    plt.xlabel(u'日期')  # 横坐标名称
    plt.ylabel(u'注册人数')  # 纵坐标名称
    plt.plot(x, num_of_users, 'ro-')
    plt.xticks(x, data, rotation=90)
    plt.margins(0.008)
    plt.subplots_adjust(bottom=0.2)
    plt.show()
reg_statistic_dis()
def level_statistic():  #统计各个等级的 流失 和 非流失 人数，并写进文件
    level_dic_0={}
    level_dic_1 = {}
    #count=0
    f=open('E:\8-22_Ubi_data\data_analyze\level_analyze\\for_28model_level.csv','r')
    for line in f.readlines():
        #count+=1
        line = line.split(',')
        line[1]=line[1].strip()
        if line[1]=='':
            line[1]=0
        else:
            line[1] =int(line[1])
        #print line[1]
        if line[0] == '0':  #0则为流失人数统计
            if line[1] not in level_dic_0:
                level_dic_0[line[1]] = 1
            else:
                level_dic_0[line[1]] +=1
        if line[0] == '1':  #为1是非流失人数统计
            if line[1] not in level_dic_1:
                level_dic_1[line[1]] = 1
            else:
                level_dic_1[line[1]] +=1
    # for key in level_dic_0:
    #     level_dic_0[key]=float(int(level_dic_0[key])/(int(level_dic_0[key]+level_dic_1[key])))
    # for key in level_dic_1:
    #     level_dic_1[key]=1-level_dic_0[key]
    #字典写入比例


    dict_0 = sorted(level_dic_0.items(), key=lambda d: d[0])  # 排序，按主键日期对其进行排序,
    dict_1 = sorted(level_dic_1.items(), key=lambda d: d[0])  # 排序，按主键日期对其进行排序,
    fw=open('E:\8-22_Ubi_data\data_analyze\level_analyze\\for_28model_level_dic_count_0.txt','w') #_1 表示非流失，改为_0表示流失人数文件
    fw1 = open('E:\8-22_Ubi_data\data_analyze\level_analyze\\for_28model_level_dic_count_1.txt', 'w')  # _1 表示非流失，改为_0表示流失人数文件
    for i in dict_0:
        fw.write(str(i[0])+'\t'+str(i[1])+'\n')
    for i in dict_1:
        fw1.write(str(i[0])+'\t'+str(i[1])+'\n')
    #print count
#level_statistic()
def level_statistic_dis(): #将各个等级的 流失 和非流失 人数画图展示出来
    data=[]
    rate_of_users_0=[]
    rate_of_users_1 = []
    f= open('E:\8-22_Ubi_data\data_analyze\level_analyze\\for_7model_level_dic_count_0.txt','r')
    f1 = open('E:\8-22_Ubi_data\data_analyze\level_analyze\\for_7model_level_dic_count_1.txt','r')
    for line in f.readlines():
        line= line.split('\t')
        data.append(line[0])
        rate_of_users_0.append((line[1]))
    for line in f1.readlines():
        line= line.split('\t')
        #data.append(line[0])
        rate_of_users_1.append((line[1]))
    x = range(len(data))
    plt.title(u'各等级流失人数-7') #图标名称
    label = [u"流失", u"非流失"]  #标注
    plt.xlabel(u'等级')    #横坐标名称
    plt.ylabel(u'人数')    #纵坐标名称
    plt.plot(x, rate_of_users_0, 'ro-')
    plt.plot(x, rate_of_users_1, 'bo-')
    plt.legend(label, loc=0, ncol=2) #label,是显示图例内容，loc是显示位置，0表示自适应，ncol表示显示几列
    plt.xticks(x, data, rotation=90)
    plt.margins(0.008)
    plt.subplots_adjust(bottom=0.2)
    fig_name = 'E:\8-22_Ubi_data\data_analyze\level_analyze\\churn_count' + '\\' + 'churn_count_7' + '.png'
    plt.savefig(fig_name)#要先保存再显示，因为显示完后会申请新的桌布，保存下来的就是空白，所以要先保存再显示
    plt.show()
#level_statistic_dis()








def friends_statistic():  #统计不同好友个数段的 流失 和 非流失 人数，并写进文件  好友段划分：0，1-10,11-20,21-30,31-40,41-50,51-60,61-70,71-80,81-90,91-100，>100
    friends_dic_0={}
    friends_dic_1={}
    f=open('E:\8-22_Ubi_data\data_analyze\\friend_analyze\\for_28model_friends.csv','r')
    for line in f.readlines():
        line = line.split(',')
        line[1]=line[1].strip()
        if line[1]=='':
            line[1]=0
        else:
            line[1] =int(line[1])

        if line[1] > 0 and line[1] <= 10:
            line[1] = 1
        if line[1] > 10 and line[1] <= 20:
            line[1] = 2
        if line[1] > 20 and line[1] <= 30:
            line[1] = 3
        if line[1] > 30 and line[1] <= 40:
            line[1] = 4
        if line[1] > 40 and line[1] <= 50:
            line[1] = 5
        if line[1] > 50 and line[1] <= 60:
            line[1] = 6
        if line[1] > 60 and line[1] <= 70:
            line[1] = 7
        if line[1] > 70 and line[1] <= 80:
            line[1] = 8
        if line[1] > 80 and line[1] <= 90:
            line[1] = 9
        if line[1] > 90 and line[1] <= 100:
            line[1] = 10
        if line[1] > 100:
            line[1] = 11
        if line[0]=='0':
            if line[1] not in friends_dic_0:
                friends_dic_0[line[1]] = 1
            else:
                friends_dic_0[line[1]] += 1

        if line[0] == '1':  #为1是非流失人数统计，改为0则为流失人数统计
            if line[1] not in friends_dic_1:
                friends_dic_1[line[1]] = 1
            else:
                friends_dic_1[line[1]] +=1

    dict0 = sorted(friends_dic_0.items(), key=lambda d: d[0])  # 排序，按主键日期对其进行排序,

    dict1 = sorted(friends_dic_1.items(), key=lambda d: d[0])  # 排序，按主键日期对其进行排序

    fw = open('E:\8-22_Ubi_data\data_analyze\\friend_analyze\\for_28model_friends_0.txt','w') #_1 表示非流失，改为_0表示流失人数文件
    fw1 = open('E:\8-22_Ubi_data\data_analyze\\friend_analyze\\for_28model_friends_dic_1.txt', 'w')  # _1 表示非流失，改为_0表示流失人数文件
    for i in dict0:
        fw.write(str(i[0])+'\t'+str(i[1])+'\n')
    for i in dict1:
        fw1.write(str(i[0])+'\t'+str(i[1])+'\n')
#friends_statistic()
def friends_statistic_dis(): #将各个等级的 流失 和非流失 人数画图展示出来
    data=[]
    num_of_users=[]
    f= open('E:\8-22_Ubi_data\data_analyze\\friend_analyze\\for_7model_friends_dic_1.txt','r')
    for line in f.readlines():
        line= line.split('\t')
        data.append(line[0])
        num_of_users.append(int(line[1]))
    x = range(len(data))
    plt.plot(x, num_of_users, 'ro-')
    plt.xticks(x, data, rotation=90)
    plt.margins(0.008)
    plt.subplots_adjust(bottom=0.2)
    plt.show()
#friends_statistic_dis()