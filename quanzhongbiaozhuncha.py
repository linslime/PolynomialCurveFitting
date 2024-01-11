#用于各个制作散点图


import random
import pandas as pd
flowdata = open("D:\Desktop\Data.txt", 'w+')
flowvalue = open("D:\Desktop\Value.txt", 'w+')
flowStandardDeviation = open("D:\Desktop\StandardDeviation.txt", 'w+')
resultvalue = []
resultdata = []
li = []
data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet3', names=['number','value','StandardDeviation'], usecols=[1,2,3])
da_f = data_f.values
data = [18,5,31,22,24,13,15,20,19,23]
for j in range(0,10000):
    list = []
    for i in range(0, len(data)):
        list.append(random.randint(0, 10000))
    sum = 0
    for i in list:
        sum += i
    for i in range(0, len(list)):
        list[i] = list[i] / sum
    li.append(list)

for i in li:
    valuenum = 0
    for j in range(0,len(data)):
        valuenum += i[j]*da_f[data[j]-1][1]
    resultvalue.append(valuenum)
for i in li:
    StandardDeviationnum = 0
    for j in range(0,len(data)):
        StandardDeviationnum += i[j]*da_f[data[j]-1][2]
    resultdata.append(StandardDeviationnum)
for i in range(0,10000):
    print(resultvalue[i],file=flowvalue)
    print(resultdata[i],file=flowStandardDeviation)
    print(i+1,":\t",li[i],file=flowdata)
flowvalue.close()
flowdata.close()
flowStandardDeviation.close()
