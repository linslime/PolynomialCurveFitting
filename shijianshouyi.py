#用于计算各年各支股票的受益率

import math
import pandas as pd
flow = open("D:\Desktop\T1.txt", 'w+')
for i in range(0,45):
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['dates', 'value'],
                           usecols=[i * 2, i * 2 + 1])
    data_f['delta'] = pd.to_datetime(data_f['dates']) - pd.to_datetime('2016-01-01')
    data_f['delta'] = data_f['delta'].dt.days
    data_f['de'] = pd.to_datetime('2017-03-01') - pd.to_datetime(data_f['dates'])
    data_f['de'] = data_f['de'].dt.days
    da_f = data_f.values
    list = []
    li = []
    sum = 0
    for j in da_f:
        if j[2] < 0:
            continue
        if j[3] < 0:
            continue
        if math.isnan(j[1]):
            break
        list.append(j[1])
    for j in range(1,len(list)):
        li.append(list[j] / list[j - 1] - 1)
    for j in li:
        sum += j
    e = sum / len(li)
    print(e*250,file=flow)
flow.close