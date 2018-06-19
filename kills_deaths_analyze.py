# -*- coding:utf-8 *-*
# @Time    : 2017/10/22 0022 20:50
# @Author  : LQY
# @File    : kills_deaths_analyze.py
# @Software: PyCharm Community Edition

from __future__ import division
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']



def kills_deaths_statistic_dis(): #将杀敌数作为x.死亡数作为y,画出流失 和非流失 散点图
    data1=[]
    data2=[]
    rate_of_users_0=[]
    rate_of_users_1 = []
    f= open('E:\8-22_Ubi_data\data_analyze\kills_deaths\\for_7model_mean_kills_deaths.csv','r')
    for line in f.readlines():
        line= line.split(',')
        line[1] = line[1].strip()
        if line[1] == '':
            line[1] = 0.0
        else:
            line[1] = float(line[1])
        line[2] = line[2].strip()
        if line[2] == '':
            line[2] = 0.0
        else:
            line[2]= float(line[2])
        if line[0]=='0':
            data1.append(line[1])
            rate_of_users_0.append(line[2])
        if line[0]=='1':
            data2.append(line[1])
            rate_of_users_1.append(line[2])
    #print data1,data2,rate_of_users_0,rate_of_users_1
    #x = range(data.)
    ax1=plt.subplot(121)
    plt.title(u'流失用户杀敌数与死亡数分布-7')
    #plt.title(u'杀敌数与死亡数的分布-28') #图标名称
    #label = [u"流失", u"非流失"]  #标注
    plt.xlabel(u'杀敌数')    #横坐标名称
    plt.ylabel(u'死亡数')    #纵坐标名称
    plt.sca(ax1)
    plt.plot(data1,rate_of_users_0, 'r.')

    ax2=plt.subplot(122)
    plt.title(u'非流失用户杀敌数与死亡数分布-7')
    plt.xlabel(u'杀敌数')
    plt.ylabel(u'死亡数')
    plt.sca(ax2)
    plt.plot(data2, rate_of_users_1, 'b.')
    #plt.legend(label, loc=0, ncol=2) #label,是显示图例内容，loc是显示位置，0表示自适应，ncol表示显示几列
    #plt.xticks(x, data, rotation=90)
    plt.margins(0.008)
    plt.subplots_adjust(bottom=0.2)
    fig_name = 'E:\8-22_Ubi_data\data_analyze\\kills_deaths\\churn_count' + '\\' + 'churn_count_7_compare' + '.png'
    plt.savefig(fig_name)#要先保存再显示，因为显示完后会申请新的桌布，保存下来的就是空白，所以要先保存再显示
    plt.show()
#kills_deaths_statistic_dis()
def gc_spent_deaths_dis(): #将杀敌数作为x.死亡数作为y,画出流失 和非流失 散点图
    data1=[]
    data2=[]
    rate_of_users_0=[]
    rate_of_users_1 = []
    f= open('E:\8-22_Ubi_data\data_analyze\gc_spent_deaths\\for_7model_gc_spent_deaths.csv','r')
    for line in f.readlines():
        line= line.split(',')
        #print line
        line[1] = line[1].strip()
        if line[1] == '':
            line[1] = 0.0
        else:
            line[1] = float(line[1])
        line[2] = line[2].strip()
        if line[2] == '':
            line[2] = 0.0
        else:
            line[2]= float(line[2])
        if line[0]=='0':
            data1.append(line[1])
            rate_of_users_0.append(line[2])
        if line[0]=='1':
            data2.append(line[1])
            rate_of_users_1.append(line[2])
    #print data1,data2,rate_of_users_0,rate_of_users_1
    #x = range(data.)
    #label = [u"流失", u"非流失"]  # 标注

    ax1=plt.subplot(121) #子图申请完之后就需要给其命名，声明坐标
    plt.title(u'流失用户-7')
    xlabel(u'gc币花费数')  # 横坐标名称
    ylabel(u'死亡数')


    ax2=plt.subplot(122)
    plt.title(u'非流失用户-7')
    xlabel(u'gc币花费数')    #横坐标名称
    ylabel(u'死亡数')    #纵坐标名称


    plt.sca(ax1)
    plt.plot(data1,rate_of_users_0, 'r.')#,alpha=0.5)
    #plt.legend(label[0], loc=0, ncol=1)  # label,是显示图例内容，loc是显示位置，0表示自适应，ncol表示显示几列


    plt.sca(ax2)
    plt.plot(data2, rate_of_users_1, 'b.')#,alpha=0.3)
    #plt.legend(label[1], loc=0, ncol=1)  # label,是显示图例内容，loc是显示位置，0表示自适应，ncol表示显示几列
    # plt.scatter()

    #plt.xticks(x, data, rotation=90)
    plt.margins(0.008)
    plt.subplots_adjust(bottom=0.2) #整个图向上调整0.2
    fig_name = 'E:\8-22_Ubi_data\data_analyze\gc_spent_deaths\\churn_count' + '\\' + 'churn_count_7' + '.png'
    plt.savefig(fig_name,facecolor=None)#要先保存再显示，因为显示完后会申请新的桌布，保存下来的就是空白，所以要先保存再显示
    plt.show()
gc_spent_deaths_dis()








