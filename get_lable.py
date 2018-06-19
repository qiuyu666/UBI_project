# -*- coding:utf-8 *-*
# @Time    : 2017/9/11 0011 19:31
# @Author  : LQY
# @File    : get_lable.py
# @Software: PyCharm Community Edition
from datetime import datetime





def get_14model(date1,date2,date3,path):

    user_dic = {}
    user_firstlogin_dic = {}  # value存放 所有用户的第一次登录时间
    user_for_7model = {}  # value存放标签
    user_for_14model = {}
    user_for_21model = {}
    user_for_28model = {}
    # date1 = '2014-12-01'
    # date2 = '2014-12-14'
    # date3 = '2014-12-28'
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
                        if 6<=(datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days<13:  #7<=登录天数<14
                            user_for_7model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
                        if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days==13:  #7<=登录天数<14
                            user_for_14model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
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
                                user_for_14model[line[0]] = 0 # 连续14天未登录又回来的打负标签0
                            else:
                                user_for_14model[line[0]] = 1  # date3后又登陆过的，打为正标签1
                                user_dic[line[0]] = line[3]

    print 'at here'

    for key in user_dic:
        if key in user_for_7model:
            if user_for_7model[key] == user_dic[key]:
                user_for_7model[key] = 0  # 没有再登录过的，两者值是一样的，打为负标签0
        if key in user_for_14model:
            if user_for_14model[key] == user_dic[key]:
                user_for_14model[key] = 0  # 没有再登录过的，两者值是一样的，打为负标签0


    # print user_dic['2077532'],user_for_7model['2077532']

    fw = open(path+'\\user_for_7model_14', 'w')
    fw1 = open(path+'\\user_for_14model_14', 'w')
    for key in user_for_7model:
        if user_for_7model[key] != 2:
            fw.write(str(key) + '\t' + str(user_for_7model[key]) + '\n')
    for key in user_for_14model:
        if user_for_14model[key] != 2:
            fw1.write(str(key) + '\t' + str(user_for_14model[key]) + '\n')

    print 'finish'
# get_14model()

def get_21model(date1,date2,date3,path):

    user_dic = {}
    user_for_7model = {}  # value存放标签
    user_for_14model = {}
    user_for_21model = {}
    user_for_28model = {}
    # date1 = '2014-11-01'
    # date2 = '2014-11-21'
    # date3 = '2014-12-05'
    # date1 = '2014-12-01'
    # date2 = '2014-12-21'
    # date3 = '2015-01-04'
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
                        if 6<=(datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days<13:  #注意 第一次登录在11月14号登录的用户会被写到文件里两次
                            user_for_7model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
                        else:
                            if 13<=(datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3], '%Y-%m-%d')).days<20:
                                user_for_14model[line[0]]=line[3]
                                user_dic[line[0]]=line[3]
                            else:
                                if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3], '%Y-%m-%d')).days == 20:
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
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days <= 14:
                                user_for_14model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_14model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days>13:
                                user_for_14model[line[0]] = 2 #针对在时间窗口内流失了，时间窗口外又回来的，在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_14model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                                else:
                                    user_for_14model[line[0]] = 1  # date3后又登陆过的，打为正标签
                                    user_dic[line[0]] = line[3]
                    if line[0] in user_for_21model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days <= 14:
                                user_for_21model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_21model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 13:
                                user_for_21model[line[0]] = 2  #在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_21model[line[0]] = 0  # 窗口外连续14天未登录又回来的打负标签0
                                else:
                                    user_for_21model[line[0]] = 1  # date3后又登陆过的，打为正标签1
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
                        if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key],'%Y-%m-%d')).days > 13:
                            user_for_21model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                        else:
                            user_for_21model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0




                        # print user_dic['2077532'],user_for_7model['2077532']

    fw = open(path+'\\user_for_7model_21', 'w')
    fw1 = open(path+'\\user_for_14model_21', 'w')
    fw2 = open(path+'\\user_for_21model_21', 'w')
    for key in user_for_7model:
        if user_for_7model[key] != 2:
            fw.write(str(key) + '\t' + str(user_for_7model[key]) + '\n')
    for key1 in user_for_14model:
        if user_for_14model[key1] != 2:
            fw1.write(str(key1) + '\t' + str(user_for_14model[key1]) + '\n')
    for key1 in user_for_21model:
        if user_for_21model[key1] != 2:
            fw2.write(str(key1) + '\t' + str(user_for_21model[key1]) + '\n')


    print 'finish'



def get_28model(date1,date2,date3,path):

    user_dic = {}
    user_firstlogin_dic = {}  # value存放 所有用户的第一次登录时间
    user_for_7model = {}  # value存放标签
    user_for_14model = {}
    user_for_21model = {}
    user_for_28model = {}

    # date1 = '2014-11-01'
    # date2 = '2014-11-28'
    # date3 = '2014-12-12'
    # date1 = '2014-12-01'
    # date2 = '2014-12-28'
    # date3 = '2015-01-11'
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
                        if 6<=(datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(line[3], '%Y-%m-%d')).days<13:
                            user_for_7model[line[0]] = line[3]  # 初始标签是第一次登录时间
                            user_dic[line[0]] = line[3]
                        else:
                            if 13<=(datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3], '%Y-%m-%d')).days <20:
                                user_for_14model[line[0]]=line[3]
                                user_dic[line[0]]=line[3]
                            else:
                                if 20<=(datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3],'%Y-%m-%d')).days<27:
                                    user_for_21model[line[0]] = line[3]
                                    user_dic[line[0]] = line[3]
                                else:
                                    if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(line[3],'%Y-%m-%d')).days>=27:
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
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days <= 14:
                                user_for_14model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_14model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d')-datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days>13:
                                user_for_14model[line[0]] = 2  ##针对在时间窗口内流失了，时间窗口外又回来的，在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_14model[line[0]] = 0  # 连续14天未登录又回来的打负标签0
                                else:
                                    user_for_14model[line[0]] = 1  # date3后又登陆过的，打为正标签
                                    user_dic[line[0]] = line[3]
                    if line[0] in user_for_21model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3], '%Y-%m-%d') <= datetime.strptime(date2, '%Y-%m-%d'):
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days <= 14:
                                user_for_21model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_21model[line[0]]=2 #流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 13:
                                user_for_21model[line[0]] = 2  #在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
                            else:
                                if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],'%Y-%m-%d')).days > 14:
                                    user_for_21model[line[0]] = 0  # 窗口外连续14天未登录又回来的打负标签0
                                else:
                                    user_for_21model[line[0]] = 1  # date3后又登陆过的，打为正标签1
                                    user_dic[line[0]] = line[3]
                    #user_dic[line[0]] = line[3]
                    if line[0] in user_for_28model:
                        if datetime.strptime(date1, '%Y-%m-%d') <= datetime.strptime(line[3],
                                                                                     '%Y-%m-%d') <= datetime.strptime(
                                date2, '%Y-%m-%d'):
                            if (datetime.strptime(line[3], '%Y-%m-%d') - datetime.strptime(user_dic[line[0]],
                                                                                           '%Y-%m-%d')).days <= 14:
                                user_for_28model[line[0]] = line[3]
                                user_dic[line[0]] = line[3]  # 在date1-date3之间登录的，两者value一致
                            else:
                                user_for_28model[line[0]] = 2  # 流失又回来的样本打标签2 不要了
                        else:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[line[0]], '%Y-%m-%d')).days > 13:
                                user_for_28model[line[0]] = 2  # 在打负标签0之前 先判断是不是在时间窗口内已经有14天未登录
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
                    if key in user_for_28model:
                        if user_for_28model[key] == user_dic[key]:
                            if (datetime.strptime(date2, '%Y-%m-%d') - datetime.strptime(user_dic[key],
                                                                                         '%Y-%m-%d')).days > 13:
                                user_for_28model[key] = 2  # 没有再登录过的，且在date2之前就流失的打标签2
                            else:
                                user_for_28model[key] = 0  # date1-date2之间没有流失，但在窗口后面流失的打标签0
    fw = open(path+'\\user_for_7model_28', 'w')
    fw1 = open(path+'\\user_for_14model_28', 'w')
    fw2 = open(path+'\\user_for_21model_28', 'w')
    fw3 = open(path+'\\user_for_28model_28', 'w')
    for key in user_for_7model:
        if user_for_7model[key] != 2:
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

get_14model('2014-11-01','2014-11-07','2014-11-21','E:\8-22_Ubi_data\data_deal_new\\1101-1107')
#get_21model('2014-11-01','2014-11-21','2014-12-05','E:\8-22_Ubi_data\data_deal_new\\1101-1121')
#get_28model('2014-11-01','2014-11-28','2014-12-12','E:\8-22_Ubi_data\data_deal_new\\1101-1128')
# get_28model('2014-11-01','2014-12-05','2014-12-19','E:\8-22_Ubi_data\data_deal_new\\1101-1205')
# get_28model('2014-11-01','2014-12-12','2014-12-26','E:\8-22_Ubi_data\data_deal_new\\1101-1212')
# get_28model('2014-11-01','2014-12-19','2015-01-02','E:\8-22_Ubi_data\data_deal_new\\1101-1219')
# get_28model('2014-11-01','2014-12-26','2015-01-09','E:\8-22_Ubi_data\data_deal_new\\1101-1226')
# get_28model('2014-11-01','2015-01-02','2015-01-16','E:\8-22_Ubi_data\data_deal_new\\1101-0102')
# get_28model('2014-11-01','2015-01-09','2015-01-23','E:\8-22_Ubi_data\data_deal_new\\1101-0109')
# get_28model('2014-11-01','2015-01-17','2015-01-31','E:\8-22_Ubi_data\data_deal_new\\1101-0117')
#print  (datetime.strptime('2014-12-12', '%Y-%m-%d')-datetime.strptime('2014-11-27', '%Y-%m-%d')).days




