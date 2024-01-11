#计算各支股票的夏普利率

import math

import pandas as pd
import empyrical as empyrical

flow = open("D:\Desktop\T1.txt", 'w+')

for j in range(0,45):
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['value'], usecols=[j * 2 + 1])
    da_f = data_f.values
    list = []
    li = []

    for i in da_f:

        if math.isnan(i[0]):
            break
        list.append(i[0])
    for i in range(1, len(list)):
        li.append(list[i] / list[i - 1] - 1)

    myvar = pd.Series(li)

    result = empyrical.sharpe_ratio(myvar, risk_free=0.00008, period='daily', annualization=None)
    print(result,file = flow)
flow.close()