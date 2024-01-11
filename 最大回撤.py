#用于计算各支股票的最大回撤

import math

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# data = [100, 200, 50, 300, 150, 100, 200]
# print(np.maximum.accumulate(data))  # [100 200 200 300 300 300 300]
data = []
flow = open("D:\Desktop\T1.txt", 'w+')
for j in range(0,45):
    # 导入股票数据
    data = []
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['dates', 'value'],usecols=[j * 2, j * 2 + 1])
    data_f['delta'] = pd.to_datetime(data_f['dates']) - pd.to_datetime('2015-05-31')
    data_f['delta'] = data_f['delta'].dt.days
    data_f['de'] = pd.to_datetime('2018-05-31') - pd.to_datetime(data_f['dates'])
    data_f['de'] = data_f['de'].dt.days
    da_f = data_f.values
    for i in da_f:
        if math.isnan(i[1]):
            break
        if i[2] < 0:
            continue
        if i[3] < 0:
            continue

        data.append(i[1])

    # data = np.random.randn(100).cumsum()

    index_j = np.argmax(np.maximum.accumulate(data) - data)  # 结束位置

    index_i = np.argmax(data[:index_j])  # 开始位置

    d = data[index_j] - data[index_i]  # 最大回撤
    print(d,file=flow)
flow.close()
# # 绘制图像
#
# plt.plot(data)
# plt.plot([index_i, index_j], [data[index_i], data[index_j]], 'o', color="r", markersize=10)
# plt.show()