#用于计算各年各股票的标准差


import math


import pandas as pd
flow = open("D:\Desktop\T1.txt", 'w+')
for i in range(0,45):
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['dates', 'value'],
                           usecols=[i * 2, i * 2 + 1])
    data_f['delta'] = pd.to_datetime(data_f['dates']) - pd.to_datetime('2017-03-01')
    data_f['delta'] = data_f['delta'].dt.days
    data_f['de'] = pd.to_datetime('2018-06-01') - pd.to_datetime(data_f['dates'])
    data_f['de'] = data_f['de'].dt.days
    da_f = data_f.values
    list = []
    for j in da_f:
        if j[2] < 0:
            continue
        if j[3] < 0:
            continue
        if math.isnan(j[1]):
            break
        list.append(j[1])
    e = 0
    num = 0
    for j in list:
        e += j
    e = e / len(list)

    d = 0
    for j in list:
        d += (j - e) * (j - e)
    d = pow(d / len(list), 0.5)
    print(d,file = flow)
flow.close