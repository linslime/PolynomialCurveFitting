import math

import pandas as pd
import empyrical as empyrical

flow = open("D:\Desktop\T2.txt", 'w+')

for j in range(0,45):
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['value'], usecols=[j * 2 + 1])
    da_f = data_f.values
    list = []
    li = []
    sum = 0
    for i in da_f:

        if math.isnan(i[0]):
            break
        list.append(i[0])
    for i in range(1, len(list)):
        li.append(list[i] / list[i - 1] - 1)
    for i in li:
        sum += i
    e = sum/len(li)

    print(e * 250,file = flow)
flow.close()