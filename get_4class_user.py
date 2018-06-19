# -*- coding:utf-8 *-*
# @Time    : 2017/9/5 0005 10:21
# @Author  : LQY
# @File    : get_4class_user.py
# @Software: PyCharm Community Edition
from datetime import datetime

def get_7model():
    """

    :param date1:
    :param date2:
    :param date3:
    :param date4:
    :return:
    """
    user_dic={}
    user_firstlogin_dic={}  #value存放 所有用户的第一次登录时间
    user_for_7model={}  #value存放标签
    # user_for_14model = {}
    # user_for_21model = {}
    # user_for_28model = {}
    date1='2014-12-01'
    date2='2014-12-07'
    date3='2014-12-21'
    # with open('E:\\8-22_Ubi_data\\data_deal\\firt_login_date','r') as flog:
    #     for li in flog.readlines():
    #         li = li.strip().split('\t')
    #         user_firstlogin_dic[li[0]] = li[1]

    with open('E:\wash_data\washfinal_2014_11.12\\1int_user_login','r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if line[0] not in user_dic:
                if datetime.strptime(date1,'%Y-%m-%d')<=datetime.strptime(line[3],'%Y-%m-%d')<=datetime.strptime(date2,'%Y-%m-%d'):
                    user_for_7model[line[0]] =line[3]  #初始标签是第一次登录时间
                    user_dic[line[0]]=line[3]
            else:
                if datetime.strptime(date1,'%Y-%m-%d')<=datetime.strptime(line[3],'%Y-%m-%d')<=datetime.strptime(date2,'%Y-%m-%d'):
                    user_for_7model[line[0]]=line[3]
                    user_dic[line[0]]=line[3]  #在date1-date2之间登录的，两者value一致
                else:
                    if (datetime.strptime(line[3],'%Y-%m-%d')-datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days>14:
                        user_for_7model[line[0]]=0 #连续14天未登录又回来的打负标签0
                    else:
                        user_for_7model[line[0]]=1 #date2后又登陆过的，打为正标签
                        user_dic[line[0]]=line[3]

    for key in user_dic:
        if user_for_7model[key]==user_dic[key]:
            user_for_7model[key]=0 #没有再登录过的，两者值是一样的，打为负标签

    fw =open('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_7','w')
    for key in user_for_7model:
        if user_for_7model[key] != 2:
            fw.write(str(key)+'\t'+str(user_for_7model[key])+'\n')


#get_7model()




def get_14model():

    user_dic = {}
    user_firstlogin_dic = {}  # value存放 所有用户的第一次登录时间
    user_for_7model = {}  # value存放标签
    user_for_14model = {}
    user_for_21model = {}
    user_for_28model = {}
    date1 = '2014-12-01'
    date2 = '2014-12-14'
    date3 = '2014-12-28'
    # with open('E:\\8-22_Ubi_data\\data_deal\\firt_login_date','r') as flog:
    #     for li in flog.readlines():
    #         li = li.strip().split('\t')
    #         user_firstlogin_dic[li[0]] = li[1]

    with open('E:\wash_data\washfinal_2014_11.12\\1int_user_login', 'r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date3, '%Y-%m-%d'):
                if line[0] not in user_dic:
                    if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                        if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days<7:  #注意 第一次登录在11月7号登录的用户会被写到文件里两次
                            user_for_7model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
                        else:
                            user_for_14model[line[0]]=line[3]
                            user_dic[line[0]]=line[3]
                else:
                    if line[0] in user_for_7model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            user_for_7model[line[0]] = line[3]
                            user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                        else:
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                user_for_7model[line[0]] = 0 # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_7model[line[0]] = 1  # date3后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]
                    if line[0] in user_for_14model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            user_for_14model[line[0]] = line[3]
                            user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                        else:
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                user_for_14model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_14model[line[0]] = 1  # date3后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]
    print 'at here'

    for key in user_dic:
        if key in user_for_7model:
            if user_for_7model[key] == user_dic[key]:
                user_for_7model[key] = 0  # 没有再登录过的，两者值是一样的，打为负标签0
        else:
            if user_for_14model[key] == user_dic[key]:
                user_for_14model[key] = 0  # 没有再登录过的，两者值是一样的，打为负标签0


    # print user_dic['2077532'],user_for_7model['2077532']

    fw = open('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_14', 'w')
    fw1 = open('E:\\8-22_Ubi_data\\data_deal\\user_for_14model_14', 'w')
    for key in user_for_7model:
        if user_for_7model[key] != 2:
            fw.write(str(key) + '\t' + str(user_for_7model[key]) + '\n')
    for key1 in user_for_14model:
        if user_for_14model[key1] != 2:
            fw1.write(str(key1) + '\t' + str(user_for_14model[key1]) + '\n')
    print 'finish'
# get_14model()

def get_21model():

    user_dic = {}
    user_for_7model = {}  # value存放标签
    user_for_14model = {}
    user_for_21model = {}
    user_for_28model = {}
    # date1 = '2014-11-01'
    # date2 = '2014-11-21'
    # date3 = '2014-12-05'
    date1 = '2014-12-01'
    date2 = '2014-12-21'
    date3 = '2015-01-04'
    # with open('E:\\8-22_Ubi_data\\data_deal\\firt_login_date','r') as flog:
    #     for li in flog.readlines():
    #         li = li.strip().split('\t')
    #         user_firstlogin_dic[li[0]] = li[1]

    with open('E:\wash_data\washfinal_2014_11.12\\1int_user_login', 'r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date3, '%Y-%m-%d'):
                if line[0] not in user_dic:
                    if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                        if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days < 7:  #注意 第一次登录在11月14号登录的用户会被写到文件里两次
                            user_for_7model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3], '%Y-%m-%d')).days < 14:
                                user_for_14model[line[0]]=line[3]
                                user_dic[line[0]]=line[3]
                            else:
                                user_for_21model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]

                else:
                    if line[0] in user_for_7model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            user_for_7model[line[0]] = line[3]
                            user_dic[line[0]] = line[3]  # 在date1-date2之间登录的，两者value一致
                        else:
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                user_for_7model[line[0]] = 0 # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_7model[line[0]] = 1  # date2后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]
                    if line[0] in user_for_14model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            user_for_14model[line[0]] = line[3]
                            user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                        else:
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                user_for_14model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_14model[line[0]] = 1  # date3后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]
                    if line[0] in user_for_21model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days <= 14:
                                user_for_21model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_21model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days>13:
                                user_for_21model[line[0]] = 2 #针对在时间窗口内流失了，时间窗口外又回来的，在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_21model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                                else:
                                    user_for_21model[line[0]] = 1  # date3后又登陆过的，打为正标签
                                    user_dic[line[0]] = line[3]
    print 'at here'

    for key in user_dic:
        if key in user_for_7model:
            if user_for_7model[key] == user_dic[key]:
                if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(user_dic[key], '%Y-%m-%d')).days>13:
                    user_for_7model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                else:
                    user_for_7model[key] = 0 #date1-date2之间没有流失，但在窗口后面流失的打标签0

        else:
            if key in user_for_14model:
                if user_for_14model[key] == user_dic[key]:
                    if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key], '%Y-%m-%d')).days > 13:
                        user_for_14model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                    else:
                        user_for_14model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0

            else:
                if user_for_21model[key] == user_dic[key]:
                    if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key], '%Y-%m-%d')).days > 13:
                        user_for_21model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                    else:
                        user_for_21model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0



                        # print user_dic['2077532'],user_for_7model['2077532']

    fw = open('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_21', 'w')
    fw1 = open('E:\\8-22_Ubi_data\\data_deal\\user_for_14model_21', 'w')
    fw2 = open('E:\\8-22_Ubi_data\\data_deal\\user_for_21model_21', 'w')
    for key in user_for_7model:
        if user_for_7model[key] != 2:
            fw.write(str(key) + '\t' + str(user_for_7model[key]) + '\n')
    for key1 in user_for_14model:
        if user_for_14model[key1] != 2:
            fw1.write(str(key1) + '\t' + str(user_for_14model[key1]) + '\n')
    for key in user_for_21model:
        if user_for_21model[key] != 2:
            fw2.write(str(key) + '\t' + str(user_for_21model[key]) + '\n')
    print 'finish'



def get_28model():

    user_dic = {}
    user_firstlogin_dic = {}  # value存放 所有用户的第一次登录时间
    user_for_7model = {}  # value存放标签
    user_for_14model = {}
    user_for_21model = {}
    user_for_28model = {}
    # date1 = '2014-11-01'
    # date2 = '2014-11-28'
    # date3 = '2014-12-12'
    date1 = '2014-12-01'
    date2 = '2014-12-28'
    date3 = '2015-01-11'
    # with open('E:\\8-22_Ubi_data\\data_deal\\firt_login_date','r') as flog:
    #     for li in flog.readlines():
    #         li = li.strip().split('\t')
    #         user_firstlogin_dic[li[0]] = li[1]

    with open('E:\wash_data\washfinal_2014_11.12\\1int_user_login', 'r') as f:
        for line in f.readlines():
            line = line.strip().split('\t')
            if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date3, '%Y-%m-%d'):
                if line[0] not in user_dic:
                    if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                        if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days<7:  #注意 第一次登录在11月14号登录的用户会被写到文件里两次
                            user_for_7model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3], '%Y-%m-%d')).days <14:
                                user_for_14model[line[0]]=line[3]
                                user_dic[line[0]]=line[3]
                            else:
                                if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3],'%Y-%m-%d')).days <21:
                                    user_for_21model[line[0]] = line[3]
                                    user_dic[line[0]] = line[3]
                                else:
                                    user_for_28model[line[0]] = line[3]
                                    user_dic[line[0]] = line[3]
                else:
                    if line[0] in user_for_7model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            user_for_7model[line[0]] = line[3]
                            user_dic[line[0]] = line[3]  # 在date1-date2之间登录的，两者value一致
                        else:
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                user_for_7model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_7model[line[0]] = 1 # date2后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]
                    if line[0] in user_for_14model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            user_for_14model[line[0]] = line[3]
                            user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                        else:
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                user_for_14model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_14model[line[0]] = 1 # date3后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]
                    if line[0] in user_for_21model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days <= 14:
                                user_for_21model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_21model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days>13:
                                user_for_21model[line[0]] = 2  ##针对在时间窗口内流失了，时间窗口外又回来的，在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_21model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                                else:
                                    user_for_21model[line[0]] = 1  # date3后又登陆过的，打为正标签
                                    user_dic[line[0]] = line[3]
                    if line[0] in user_for_28model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days <= 14:
                                user_for_28model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_28model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 13:
                                user_for_28model[line[0]] = 2  #在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_28model[line[0]] = 0  # 窗口外连续14天未登录又回来的打负标签0
                                else:
                                    user_for_28model[line[0]] = 1  # date3后又登陆过的，打为正标签1
                                    user_dic[line[0]] = line[3]
    print 'at here'

    for key in user_dic:
        if key in user_for_7model:
            if user_for_7model[key] == user_dic[key]:
                if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(user_dic[key], '%Y-%m-%d')).days>13:
                    user_for_7model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                else:
                    user_for_7model[key] = 0 #date1-date2之间没有流失，但在窗口后面流失的打标签0

        else:
            if key in user_for_14model:
                if user_for_14model[key] == user_dic[key]:
                    if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key], '%Y-%m-%d')).days > 13:
                        user_for_14model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                    else:
                        user_for_14model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0

            else:
                if key in user_for_21model:
                    if user_for_21model[key] == user_dic[key]:
                        if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key], '%Y-%m-%d')).days > 13:
                            user_for_21model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                        else:
                            user_for_21model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0

                else:
                    if user_for_28model[key] == user_dic[key]:
                        if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key],'%Y-%m-%d')).days > 13:
                            user_for_28model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                        else:
                            user_for_28model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0




                            # print user_dic['2077532'],user_for_7model['2077532']

    fw = open('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_28', 'w')
    fw1 = open('E:\\8-22_Ubi_data\\data_deal\\user_for_14model_28', 'w')
    fw2 = open('E:\\8-22_Ubi_data\\data_deal\\user_for_21model_28', 'w')
    fw3 = open('E:\\8-22_Ubi_data\\data_deal\\user_for_28model_28', 'w')
    for key in user_for_7model:
        if user_for_7model[key]!=2:
            fw.write(str(key) + '\t' + str(user_for_7model[key]) + '\n')
    for key1 in user_for_14model:
        if user_for_14model[key1] != 2:
            fw1.write(str(key1) + '\t' + str(user_for_14model[key1]) + '\n')
    for key in user_for_21model:
        if user_for_21model[key] != 2:
            fw2.write(str(key) + '\t' + str(user_for_21model[key]) + '\n')
    for key in user_for_28model:
        if user_for_28model[key] != 2:
            fw3.write(str(key) + '\t' + str(user_for_28model[key]) + '\n')
    print 'finish'

get_7model()
get_14model()
get_21model()
get_28model()
#
# def remove_same(filename):
#     user_dic={}
#     con=0
#     same=0
#     with open(filename, 'r') as f:
#         for line in f.readlines():
#             line = line.strip().split('\t')
#             if line[0] not in user_dic:
#                 user_dic[line[0]]=line[1]
#             else:
#                 if user_dic[line[0]]!=line[1]:
#                     print line[0],line[1],user_dic[line[0]]
#                     con += 1
#                 else:
#                     same += 1
#
#     print con,same
#     print 'finish'
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_7')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_14')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_21')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_7model_28')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_14model_14')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_14model_21')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_14model_28')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_21model_21')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_21model_28')
# remove_same('E:\\8-22_Ubi_data\\data_deal\\user_for_28model_28')


