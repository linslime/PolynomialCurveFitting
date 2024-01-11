#用于计算各支股票总体的收益率并按顺序打印出来

import math

import pandas as pd
import empyrical as empyrical

flow = open("D:\Desktop\T2.txt", 'w+')
a = []

result = []
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
    a = []
    a.append(j+1)
    a.append(e*250)
    result.append(a)

for i in range(0,len(result) - 1):
    max = i
    for j in range(i+1,len(result)):
        if result[j][1] > result[max][1]:
            max = j
    if i != max:
        result[max], result[i] = result[i], result[max]
for i in result:
    print("第",i[0],"只股票受益率：",i[1],file = flow)
flow.close()