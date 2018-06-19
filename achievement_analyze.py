# -*- coding:utf-8 *-*
# @Time    : 2017/10/22 0022 15:12
# @Author  : LQY
# @File    : achievement_analyze.py
# @Software: PyCharm Community Edition
# -*- coding:utf-8 *-*
# @Time    : 2017/8/25 0025 15:28
# @Author  : LQY
# @File    : data_display.py
# @Software: PyCharm Community Edition
from __future__ import division
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']


def achievement_statistic():  #统计各个等级的 流失 和 非流失 人数，并写进文件
    level_dic_0={}
    level_dic_1 = {}
    #count=0
    f=open('E:\8-22_Ubi_data\data_analyze\\achievement_analyze\\for_28model_achievement.csv','r')
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
    fw=open('E:\8-22_Ubi_data\data_analyze\\achievement_analyze\\for_28model_achievement_dic_count_0.txt','w') #_1 表示非流失，改为_0表示流失人数文件
    fw1 = open('E:\8-22_Ubi_data\data_analyze\\achievement_analyze\\for_28model_achievement_dic_count_1.txt', 'w')  # _1 表示非流失，改为_0表示流失人数文件
    for i in dict_0:
        fw.write(str(i[0])+'\t'+str(i[1])+'\n')
    for i in dict_1:
        fw1.write(str(i[0])+'\t'+str(i[1])+'\n')
    #print count
#achievement_statistic()
def achievement_statistic_dis(): #将各个等级的 流失 和非流失 人数画图展示出来
    data1=[]
    data2=[]
    rate_of_users_0=[]
    rate_of_users_1 = []
    flag0=0
    flag1=0
    f= open('E:\8-22_Ubi_data\data_analyze\\achievement_analyze\\for_28model_achievement_dic_count_0.txt','r')
    f1 = open('E:\8-22_Ubi_data\data_analyze\\achievement_analyze\\for_28model_achievement_dic_count_1.txt','r')
    for line in f.readlines():
        line= line.split('\t')
        if flag0==1:
            data1.append(line[0])
            #rate_of_users_0.append(log2(int(line[1])))
            rate_of_users_0.append(int(line[1]))
        flag0=1
    for line in f1.readlines():
        line= line.split('\t')
        if flag1==1:
            data2.append(line[0])
            #rate_of_users_1.append(log2(int(line[1])))
            rate_of_users_1.append(int(line[1]))
        flag1=1
    #x = range(data.)
    plt.title(u'不同成就的流失人数-28') #图标名称
    label = [u"流失", u"非流失"]  #标注
    plt.xlabel(u'获取成就个数')    #横坐标名称
    plt.ylabel(u'人数')    #纵坐标名称
    plt.plot(data1,rate_of_users_0, 'r.')
    plt.plot(data2, rate_of_users_1, 'b.')
    plt.legend(label, loc=0, ncol=2) #label,是显示图例内容，loc是显示位置，0表示自适应，ncol表示显示几列
    #plt.xticks(x, data, rotation=90)
    plt.margins(0.008)
    plt.subplots_adjust(bottom=0.2)
    fig_name = 'E:\8-22_Ubi_data\data_analyze\\achievement_analyze\\churn_count' + '\\' + 'churn_count_28' + '.png'
    plt.savefig(fig_name)#要先保存再显示，因为显示完后会申请新的桌布，保存下来的就是空白，所以要先保存再显示
    plt.show()
achievement_statistic_dis()








