#用于计算各支股票净值低于0.98的概率

import math

import pandas as pd
import empyrical as empyrical

flow = open("D:\Desktop\T1.txt", 'w+')
key = 0.98
list = []
li = []
result = []
for j in range(0,45):
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['value'], usecols=[j * 2 + 1])
    da_f = data_f.values
    list = []
    li = []

    for i in da_f:

        if math.isnan(i[0]):
            break
        list.append(i[0])
    temp = list[0]
    sum = 0
    for i in list:
        if i/temp < key:
            sum += 1
    a=[]
    a.append(j + 1)
    a.append(sum/len(list))
    result.append(a)
# print(result)
for i in range(0,len(result) - 1):
    max = i
    for j in range(i+1,len(result)):
        if result[j][1] > result[max][1]:
            max = j
    if i != max:
        result[max], result[i] = result[i], result[max]
for i in result:
    print("第",i[0],"只股票低于" ,key,"概率：",i[1],file = flow)
flow.close()


