# -*- coding:utf-8 -*-
import numpy
import pandas


def load_data(path):

    df = pandas.read_csv (path)
    df = df.dropna (axis=1, how='all')
    # df = df.fillna(df.mean(axis=0))
    df = df.fillna(0)
    label = df.label
    data = df.drop (['label'], axis=1)
    label.rename(columns='labels')

    return data, label

def discretize(data, bin):

    print(bin.ix[0], bin.ix[1], bin.ix[2], bin.ix[3], bin.ix[4])
    da = data.values
    i = 0
    da = numpy.piecewise(da, [da <= bin.ix[1], (da > bin.ix[1]) & (da <= bin.ix[2]), (da > bin.ix[2]) & (da <= bin.ix[3]), (da > bin.ix[3]) & (da <= bin.ix[4])], [0, 1, 2, 3])
    data = pandas.DataFrame(da, index=data.index)

    print('end discretize')
    return data


def Threshold(data, label):

    df = pandas.DataFrame (data.describe (percentiles=[0.25, 0.5, 0.75]))
    for i in range(df.shape[1]):
        print(df.columns[i],i)
        # or df.iloc[:, i].loc['67%'] == df.iloc[:, i].loc['max']
        if df.iloc[:, i].loc['25%'] == df.iloc[:, i].loc['50%'] and df.iloc[:, i].loc['25%'] == df.iloc[:, i].loc['min']:
            data = data.drop(df.columns[i], axis=1)
        elif df.iloc[:, i].loc['25%'] == df.iloc[:, i].loc['50%'] \
                or df.iloc[:, i].loc['25%'] == df.iloc[:, i].loc['min'] \
                or df.iloc[:, i].loc['50%'] == df.iloc[:, i].loc['75%'] \
                or df.iloc[:, i].loc['75%'] == df.iloc[:, i].loc['max']:
            data.ix[:, df.columns[i]] = discretize(data.ix[:, df.columns[i]], df.ix['min':'max', i])
        else:
            data.ix[:, df.columns[i]] = pandas.qcut(data.ix[:, df.columns[i]], 4, labels=False)

    print (data.columns)
    data = data.dropna(axis=1, how='all')
    data = pandas.concat((data, label), axis=1)
    data.to_csv('discretize_28.csv ')

    print('end threshold.')

if __name__ == '__main__':
    data, label = load_data (r'E:\python\yubi\all_samples\for_28model_all.csv')
    Threshold(data, label)
