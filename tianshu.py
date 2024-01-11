#计算大盘的天数

import math
import pandas as pd
flow = open("D:\Desktop\T1.txt", 'w+')
#导入大盘数据
data_t = pd.read_excel(r'D:\Desktop\two.xls', sheet_name='sheet1',names=['dates','value'],usecols=[0,4])
data_t['delta'] = pd.to_datetime(data_t['dates']) - pd.to_datetime('2015-01-01')
data_t['delta'] = data_t['delta'].dt.days
da_t = data_t.values
for i in da_t:
    print(i[2],file = flow)
flow.close