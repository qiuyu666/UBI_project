# -*- coding:utf-8 *-*
# @Time    : 2017/9/3 0003 14:14
# @Author  : LQY
# @File    : get_feature.py
# @Software: PyCharm Community Edition

import pandas as pd
import numpy as np
from datetime import datetime
#import setlabel_fun as sf
'''
fileadd:待处理文件的地址路径 string类型
udict:需要处理的user词典 dict类型
keycol:主键的列（从0开始）int类型
timecol:时间列是哪一列（从0开始）,默认-1 int类型
pcol:本文件要处理的列 list类型 e.g.[1,2,3] 注意：与process操作列表对齐
process:要处理的操作列表,e.g.['sum','mean','max'],可供选择（sum,max,min,median,count,skew,var,mad,mean）
start_data:开始日期，datetime类型 默认-1
end_date:结束日期,datetime类型,datetime 默认-1
rename:最终对列的命名,list,e.g.['qwe','qwe1','qwe2']
out_name:输出名称（多线程使用）:默认1 int
#fetchfeature(fileadd,udict,keycol,pcol,process,fileadd2=-1,timecol=-1,start_date=-1,end_date=-1,rename=-1,out_name=1)
'''
def pre_process_data(raw_data,keycol,udict):
    a=raw_data[keycol].astype(np.str)
    raw_data.pop(keycol)
    raw_data.insert(keycol,keycol,a)
    data=raw_data[raw_data[keycol].isin(udict)]
    return data


def fetchfeature(fileadd,udict,keycol,pcol,process,fileadd2=-1,timecol=-1,start_date=-1,end_date=-1,rename=-1,out_name=1):
    if len(pcol)!=len(process):
        print('pcol,process match error')
        return -1
    if timecol==-1:
        raw_data = pd.read_table(fileadd,header=-1)
        data=pre_process_data(raw_data,keycol,udict)
    else:
        raw_data = pd.read_table(fileadd,header=-1,parse_dates=[timecol])
        data=pre_process_data(raw_data,keycol,udict)
    del raw_data
    if fileadd2 !=-1:
        if timecol==-1:
            raw_data2 = pd.read_table(fileadd2,header=-1)
            data2=pre_process_data(raw_data2,keycol,udict)
        else:
            raw_data2 = pd.read_table(fileadd2,header=-1,parse_dates=[timecol])
            data2=pre_process_data(raw_data2,keycol,udict)
        del raw_data2
        data=pd.concat([data,data2])
    if timecol==-1:
        data=data.sort([keycol])
    else:
        data=data.sort([keycol,timecol])
    if start_date!=-1:
        data=data[data[timecol]>=start_date]#?
    if end_date!=-1:
        data=data[data[timecol]<=end_date]
    result=pd.DataFrame(list(udict.keys()))
    c=0
#    methods = {
#           'sum': data.groupby([keycol])[pcol[c]].sum(),
#           'max': data.groupby([keycol])[pcol[c]].max(),
#           'mean': data.groupby([keycol])[pcol[c]].mean(),
#           'min': data.groupby([keycol])[pcol[c]].min(),
#           'count': data.groupby([keycol])[pcol[c]].count(),
#           'median': data.groupby([keycol])[pcol[c]].median(),
#           'skew': data.groupby([keycol])[pcol[c]].skew(),
#           'var': data.groupby([keycol])[pcol[c]].var(),
#           'mad': data.groupby([keycol])[pcol[c]].mad()
#         }
    methods = {
           'sum':lambda x: data.groupby([keycol])[pcol[x]].sum(),
           'max':lambda x: data.groupby([keycol])[pcol[x]].max(),
           'mean':lambda x: data.groupby([keycol])[pcol[x]].mean(),
           'min':lambda x: data.groupby([keycol])[pcol[x]].min(),
           'count': lambda x: data.groupby([keycol])[pcol[x]].count(),
           'median':lambda x: data.groupby([keycol])[pcol[x]].median(),
           'skew':lambda x: data.groupby([keycol])[pcol[x]].skew(),
           'var':lambda x: data.groupby([keycol])[pcol[x]].var(),
           'mad':lambda x: data.groupby([keycol])[pcol[x]].mad(),
           'ptp':lambda x: data.groupby([keycol])[pcol[x]].ptp()
         }
    for col in pcol:
        col_result=methods[process[c]](c)
        c+=1
        col_result=pd.DataFrame(col_result)
        col_result.columns=[c]
        result=result.merge(col_result,how='left',left_on=0,right_index=True)
    if rename==-1:
        result.to_csv(str(out_name)+'result.csv',index=False)
    elif len(rename)!=len(pcol):
        result.to_csv(str(out_name)+'result.csv',index=False)
    else:
        result.columns=rename
        result.to_csv(str(out_name)+'result.csv',index=False)
    return 0

#=====================================test=====================================





'''
fileadd='D:\\mym\\8-22_Ubi_data\\washdata\\washfinal_2014_11.12\\1int_user_login'
fileadd2='D:\\mym\\8-22_Ubi_data\\washdata\\washfinal_2015_01\\1int_user_login'
udict={'1000026':1,'1240':1,'1581':1,'8779':0}
keycol=0
timecol=2
pcol=[1,2]
process=['max','max']
start_date=datetime(2014,11,5)
end_date=datetime(2015,1,10)
fetchfeature(fileadd=fileadd,udict=udict,keycol=keycol,pcol=pcol,process=process,timecol=2,start_date=start_date,end_date=end_date)
fetchfeature(fileadd,udict,keycol,pcol,process,fileadd2,2,start_date,end_date,out_name=2)
'''