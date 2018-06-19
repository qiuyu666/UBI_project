#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime
def userlog_static():
    """
    统计2014-11-01和2015-01-31，这两天int_user_active_status中累积登陆次数值，得到每个用户在此期间的登陆次数，并写进文件
    :return:
    """
    user_login_dic={}
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2015_01\gro_int\int_user_active_status', 'r') as f:
        for i in range(7):
            for line in f.readlines(1048576000):
                line = line.strip().split('\t')
                if line[9]=='2015-01-31':  #截止时间戳，截止到1月31号总登陆次数统计
                    user_login_dic[line[0]] = int(line[3])
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\int_user_active_status', 'r') as f1:
        for j in range(11):
            for line1 in f1.readlines(1048576000):
                line1 = line1.strip().split('\t')
                if line1[9]=='2014-11-01':  #截止时间戳，截止到1月31号总登陆次数统计
                    if line1[0] in user_login_dic:
                        user_login_dic[line1[0]] -= int(line1[3])
                    else:
                        user_login_dic[line1[0]] = int(line1[3])
    fw = open('E:\8-22_Ubi_data\data_deal\\uselogindur.txt', 'w')
    for key in user_login_dic.keys():
        fw.write(key+'\t'+str(user_login_dic[key])+'\n')


def notloginuser_statistic():
    """
    统计在这期间登陆次数大于1次的玩家个数
    :return:
    """
    num_of_user = 0
    notplayuser_dur = 0
    haveplay_dur = 0
    with open('E:\8-22_Ubi_data\data_deal\\uselogindur.txt', 'r') as f:
        for line in f.readlines():
            num_of_user += 1
            line = line.strip().split('\t')
            if int(line[1]) <2:
                notplayuser_dur += 1
        haveplay_dur = num_of_user - notplayuser_dur
    print '总用户数为' + str(num_of_user) + '\n' + '在此期间登录游戏次数大于1次的用户为' + str(haveplay_dur) + '\n' + '在此期间没有登录过游戏次数小于2次的用户为' + str(
        notplayuser_dur) + '\n'
#notloginuser_statistic()




def userplay_write():
    """"
    统计各用户在2015-01-31 和 2014-11-01 这两天的累积完成游戏局数，并将结果存到对应文件中


     """
    with open('E:\\8-22_Ubi_data\\ncsa_hive_part_2015_01\\gro_int\\int_user_match_status', 'r') as f:
        fw = open('E:\8-22_Ubi_data\data_deal\\wplay0131.txt', 'w')
        for i in range(80):
            for line in f.readlines(104857600):  #1兆字节(mb)=1048576字节(b)
                line = line.strip().split('\t')
                if line[31]=='2015-01-31':
                    fw.write(line[0]+'\t'+line[5]+'\n')
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\int_user_match_status', 'r') as f1:
        fw1= open('E:\8-22_Ubi_data\data_deal\\wplay1101.txt', 'w')
        for j in range(160):
            for line1 in f1.readlines(104857600):
                line1 = line1.strip().split('\t')
                if line1[31] == '2014-11-01':
                    fw1.write(line1[0] + '\t' + line1[5] + '\n')


def userplay1_write():
    """
    将2015-01-31与2014-11-01这两天数据进行求差值，得到各个用户在这个时间区间的完成游戏的情况
    """
    dic_user = {}
    with open('E:\8-22_Ubi_data\data_deal\\wplay0131.txt', 'r') as f:
        for line in f.readlines():
            line = line.split('\t')
            dic_user[line[0]]=int(line[1])
    with open('E:\8-22_Ubi_data\data_deal\\wplay1101.txt','r') as f1:
        for line1 in f1.readlines():
            line1 = line1.split('\t')
            if line1[0] in dic_user:
                dic_user[line1[0]] = dic_user[line1[0]]-int(line1[1])
            else:
                dic_user[line1[0]] = int(line1[1])
    fw = open('E:\8-22_Ubi_data\data_deal\\wplaydur.txt', 'w')
    for key1 in dic_user.keys():
        fw.write(key1+'\t'+str(dic_user[key1])+'\n')
    print 'finished'

def notplayuser_statistic():
    """
    统计在这期间完成过游戏的玩家个数 和 未完成过游戏的玩家个数
    :return:
    """
    num_of_user = 0
    notplayuser_dur=0
    haveplay_dur=0
    with open('E:\8-22_Ubi_data\data_deal\\wplaydur.txt','r') as f:
        for line in f.readlines():
            num_of_user+=1
            line = line.strip().split('\t')
            if line[1]=='0':
                notplayuser_dur+=1
        haveplay_dur=num_of_user-notplayuser_dur
    print '总用户数为'+str(num_of_user)+'\n'+'在此期间玩过游戏的用户为'+str(haveplay_dur)+'\n'+'在此期间没有玩过游戏的用户为'+str(notplayuser_dur)+'\n'
#userplay_write()
#userplay1_write()
#notplayuser_statistic()


def userplaystart_write():
    """"
    统计各用户在2015-01-31 和 2014-11-01 这两天的累积的开始游戏局数，并将结果存到对应文件中


     """
    with open('E:\\8-22_Ubi_data\\ncsa_hive_part_2015_01\\gro_int\\int_user_match_status', 'r') as f:
        fw = open('E:\8-22_Ubi_data\data_deal\\wplaystart0131.txt', 'w')
        for i in range(80):
            for line in f.readlines(104857600):  # 1兆字节(mb)=1048576字节(b)
                line = line.strip().split('\t')
                if line[31] == '2015-01-31':
                    fw.write(line[0] + '\t' + line[4] + '\n')
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\int_user_match_status', 'r') as f1:
        fw1 = open('E:\8-22_Ubi_data\data_deal\\wplaystart1101.txt', 'w')
        for j in range(160):
            for line1 in f1.readlines(104857600):
                line1 = line1.strip().split('\t')
                if line1[31] == '2014-11-01':
                    fw1.write(line1[0] + '\t' + line1[4] + '\n')


def userplaystart1_write():
    """
    将2015-01-31与2014-11-01这两天数据进行求差值，得到各个用户在这个时间区间的开始游戏的情况
    """
    dic_user = {}
    with open('E:\8-22_Ubi_data\data_deal\\wplaystart0131.txt', 'r') as f:
        for line in f.readlines():
            line = line.split('\t')
            dic_user[line[0]]=int(line[1])
    with open('E:\8-22_Ubi_data\data_deal\\wplaystart1101.txt','r') as f1:
        for line1 in f1.readlines():
            line1 = line1.split('\t')
            if line1[0] in dic_user:
                dic_user[line1[0]] = dic_user[line1[0]]-int(line1[1])
            else:
                dic_user[line1[0]] = int(line1[1])
    fw = open('E:\8-22_Ubi_data\data_deal\\wplaystartdur.txt', 'w')
    for key1 in dic_user.keys():
        fw.write(key1 + '\t' + str(dic_user[key1])+'\n')
    print 'finished'


def notstartplaytuser_statistic():
    """
    统计在这期间开始过游戏的玩家个数 和 未开始过游戏的玩家个数
    :return:
    """
    num_of_user = 0
    notplayuser_dur = 0
    haveplay_dur = 0
    with open('E:\8-22_Ubi_data\data_deal\\wplaystartdur.txt', 'r') as f:
        for line in f.readlines():
            num_of_user += 1
            line = line.strip().split('\t')
            if int(line[1]) <2:
                notplayuser_dur += 1
        haveplay_dur = num_of_user - notplayuser_dur
    print '总用户数为' + str(num_of_user) + '\n' + '在此期间开始过>1把游戏的用户为' + str(haveplay_dur) + '\n' + '在此期间开始游戏次数<=1把游戏的用户个数为' + str(
        notplayuser_dur) + '\n'


#userplaystart_write()
#userplaystart1_write()
#notstartplaytuser_statistic()
#userlog_static()
#notloginuser_statistic()



def get_userfirtlogin_date():
    user_dic={}
    fw= open('E:\8-22_Ubi_data\data_deal\\firt_login_date','w')
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\int_user_login','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[0] not in user_dic:
                user_dic[line[0]] =line[3]

    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2015_01\gro_int\int_user_login', 'r') as f1:
        for line1 in f1.readlines():
            line1 = line1.strip().split('\t')
            if line1[0] not in user_dic:
                user_dic[line1[0]]=line1[3]
    for key in user_dic:
        fw.write(key + '\t' + user_dic[key] + '\n')

#get_userfirtlogin_date()



def get_userlogin_times():
    con=0
    user_dic={}
    user_login_morethan1time={}
    fw= open('E:\8-22_Ubi_data\data_deal\\login_times','w')
    fw1 = open('E:\8-22_Ubi_data\data_deal\\login_morethan_1times', 'w')
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\int_user_login','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[0] not in user_dic:
                user_dic[line[0]] =1
            else:
                user_dic[line[0]]+=1

    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2015_01\gro_int\int_user_login', 'r') as f1:
        for line1 in f1.readlines():
            line1 = line1.strip().split('\t')
            if line1[0] not in user_dic:
                user_dic[line1[0]]=1
            else:
                user_dic[line1[0]]+=1
    for key in user_dic:
        if user_dic[key]>1:
            con+=1
            user_login_morethan1time[key] = user_dic[key]
            fw1.write(key+'\t'+str(user_dic[key])+'\n')
        fw.write(key + '\t' + str(user_dic[key]) + '\n')
    print '登陆次数大于1的用户共'+str(con)+'个人'
    times=0
    with open('E:\8-22_Ubi_data\\ncsa_hive_part_2014_11.12\gro_int\int_user_login', 'r') as f2:
        for line2 in f2.readlines():
            line2 =line2.strip().split('\t')
            if line2[0] in user_login_morethan1time:
                times+=1
    print '登陆次数大于1的用户总登录记录条数为'+str(times)+'\n'


#get_userlogin_times()
# data='2014-12-21'
# da='2014-12-11'
# db='2014-12-01'
# a=datetime.strptime(da,'%Y-%m-%d')
# b=datetime.strptime(db,'%Y-%m-%d')
# c=a-b
# k=c.days
# print c.days,type(k)


#统计14天未登陆的用户
import time
def notlogin_for14days():
    user_dic={}  #value存放 所有用户的最后一次登录时间，流失又回来的记录为流失前最后一次登陆日期
    notlog_for14days={}  #存放相隔14天 又回来登陆的用户，value是登录次数
    first_login={}
    cou=0     #满足登录超过1个月，且在此期间未流失的用户个数
    con=0     #根据最后一次登录时间来判断是否是流失用户，并计数
    neg_user=0

    with open('E:\wash_data\washfinal_2014_11.12\\1int_user_login','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[0] not in user_dic:
                user_dic[line[0]] =line[3]
            else:
                if line[0] in notlog_for14days:
                    notlog_for14days[line[0]]+=1
                else:
                    this_log=datetime.strptime(line[3],'%Y-%m-%d')
                    last_log=datetime.strptime(user_dic[line[0]],'%Y-%m-%d')
                    if (this_log-last_log).days>14:   #隔了14天又登录的
                        notlog_for14days[line[0]]=1   #把user 放进14天未登录又登陆的字典，user_dic的value(最后一次登录日期)不改变，即记录流失前最后一次登录的日期
                        #user_dic[line[0]]=line[3]
                    else:
                         user_dic[line[0]] =line[3]
    # with open('E:\wash_data\washfinal_2015_01\\1int_user_login','r') as f1:
    #     for line1 in f1.readlines():
    #         line1 = line1.strip().split('\t')
    #         if line1[0] not in user_dic:
    #             user_dic[line1[0]] =line1[3]
    #         else:
    #             if line1[0] in notlog_for14days:
    #                 notlog_for14days[line1[0]]+=1
    #             else:
    #                 this_log1=datetime.strptime(line1[3],'%Y-%m-%d')
    #                 last_log1=datetime.strptime(user_dic[line1[0]],'%Y-%m-%d')
    #                 if (this_log1-last_log1).days>14:   #相隔14天又登录的
    #                     notlog_for14days[line1[0]]=1    #把user 放进14天未登录又登陆的字典，user_dic的value(最后一次登录日期)不改变，即记录流失前最后一次登录的日期
    #                     #user_dic[line1[0]]=line1[3]
    #                 else:
    #                     user_dic[line1[0]] =line1[3]
    # with open('E:\\8-22_Ubi_data\\data_deal\\firt_login_date','r') as flog:
    #     for li in flog.readlines():
    #         li = li.strip().split('\t')
    #         first_login[li[0]] = li[1]
    # for i in user_dic:
    #     if (datetime.strptime(user_dic[i],'%Y-%m-%d')-datetime.strptime(first_login[i],'%Y-%m-%d')).days > 30:
    #         cou += 1
    #     if (datetime.strptime(user_dic[i], '%Y-%m-%d') - datetime.strptime(first_login[i], '%Y-%m-%d')).days == 30:
    #         neg_user+=1
    #
    # print cou,neg_user
    for key in user_dic:
        if (datetime.strptime('2014-11-30','%Y-%m-%d')-datetime.strptime(user_dic[key],'%Y-%m-%d')).days>13:
            con+=1
    # for key in notlog_for14days:
    #     if notlog_for14days[key]>0:
    #         con+=1
    print len(notlog_for14days),con
    # fw=open('E:\8-22_Ubi_data\data_deal\\login_thelast_date','w')
    # fw1 = open('E:\8-22_Ubi_data\data_deal\\notlog_for14_user_logtimes', 'w')
    # for key in user_dic:
    #     fw.write(key+'\t'+user_dic[key]+'\n')
    # for key1 in notlog_for14days:
    #     fw1.write(key1+'\t'+str(notlog_for14days[key1])+'\n')
#notlogin_for14days()


user1={}
user2={}
con=0
f=open('E:\8-22_Ubi_data\data_deal\\notlog_for14_user_logtimes', 'r')
f1=open('E:\8-22_Ubi_data\data_deal\\notlog_for14_user_logtimes1', 'r')
for line in f.readlines():
    line=line.split('\t')
    user1[line[0]]=line[1]
for line1 in f1.readlines():
    line1=line1.split('\t')
    user2[line1[0]]=line1[1]
for key in user1:
    if key not in user2:
        con+=1
        #print key
print con
# print con,con/68918












