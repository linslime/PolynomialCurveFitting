#用于计算各支股票时间天数

import math
import pandas as pd
flow = open("D:\Desktop\T1.txt", 'w+')
#导入大盘数据
data_t = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1',names=['dates'],usecols=[2])
data_t['delta'] = pd.to_datetime(data_t['dates']) - pd.to_datetime('2015-01-01')
data_t['delta'] = data_t['delta'].dt.days
da_t = data_t.values
for i in da_t:
    if math.isnan(i[1]):
        break
    print(i[1],file = flow)
flow.close