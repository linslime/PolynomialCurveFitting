#用于计算各支股票与大盘的相关性和计算各支股票总体的标准差


import math
import pandas as pd

#导入大盘数据
data_t = pd.read_excel(r'D:\Desktop\two.xls', sheet_name='sheet1',names=['dates','value'],usecols=[1,5])
data_t['delta'] = pd.to_datetime(data_t['dates']) - pd.to_datetime('2015-01-01')
data_t['delta'] = data_t['delta'].dt.days
da_t = data_t.values

#计算股票期望
E_dapan = 0
num = 0
for j in da_t:

    if math.isnan(j[1]):
        break
    E_dapan += j[1]
    num += 1
E_dapan = E_dapan / num

#计算股票标准差
D_dapan = 0
for j in da_t:
    if math.isnan(j[1]):
        break
    D_dapan += (j[1] - E_dapan) * (j[1] - E_dapan)
D_dapan = pow(D_dapan / num, 0.5)

result = open("D:\Desktop\data.txt", 'w+')
print("大盘方差:",D_dapan, file=result)
print()


#处理各股票数据
for i in range(0,45):
    #导入股票数据
    data_f = pd.read_excel(r'D:\Desktop\one.xls', sheet_name='Sheet1', names=['dates', 'value'], usecols=[i*2, i*2 + 1])
    data_f['delta'] = pd.to_datetime(data_f['dates']) - pd.to_datetime('2015-01-01')
    data_f['delta'] = data_f['delta'].dt.days
    da_f = data_f.values

    #匹配股票与大盘数据
    list = []
    for j in da_f:

        if math.isnan(j[1]):
            break
        li = []
        li.append(j[2])
        li.append(j[1])
        for k in da_t:
            if k[2] == j[2]:
                li.append(k[1] / 4909.98)
                break
            # if j[2] < k[2]:
            #     break
        if (len(li) == 3):
            list.append(li)

    #计算相关股票期望
    Ef = 0
    num = 0
    for j in list:

        if math.isnan(j[1]):
            break
        Ef += j[1]

        num += 1
    Ef = Ef / num
    #计算相关股票标准差
    Df = 0
    for j in list:
        if math.isnan(j[1]):
            break
        Df += (j[1] - Ef) * (j[1] - Ef)
    Df = pow(Df / num, 0.5)


   #计算相关大盘期望
    Et = 0
    num = 0
    for j in list:
        if math.isnan(j[2]):
            break
        Et += j[2]
        num += 1
    Et = Et / num

    #计算相关大盘标准差
    Dt = 0.0
    for j in list:
        if math.isnan(j[2]):
            break
        Dt += (j[2] - Et) * (j[2] - Et)
    Dt = pow(Dt / num, 0.5)

    # 计算股票期望
    E = 0
    num = 0
    for j in da_f:

        if math.isnan(j[1]):
            break
        E += j[1]

        num += 1
    E = E / num

    # 计算股票标准差
    D = 0
    for j in da_f:
        if math.isnan(j[1]):
            break
        D += (j[1] - E) * (j[1] - E)
    D = pow(D / num, 0.5)

    #相关度计算
    r = 0
    for j in list:
        if math.isnan(j[1]):
            break
        r += (j[1] - Ef) * (j[2] - Et)
    r = r / (len(list) * Df * Dt)

    #结果输出
    print(r, file=result)

result.close()



