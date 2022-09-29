
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

# 根据正态分布的 3sigma法则，5-10范围的均值和方差，和[5,6,7,8,9,10]差不多
# 故：5-10范围的均值：(5+10)/2=7.5
# 标准差：(10-7.5)/3
# s = [5,6,7,8,9,10]
# mu = np.mean(s) # 均值
# sigma = np.std(s)   # 标准差
# var = np.var(s) # 方差

# 方法一
def getGaussRandomNum(min, max):
    # 比如 生成   50-100  范围内的正态分布的数，均值为75
    # 据 3 sigma 法则，取标准差为 （100-75）/3 = 8.33
    # mu, sigma = 75, 8.33
    # 30-60 mu=45 sig=(60-45)/3=5
    mu = (min + max) / 2
    sigma = (max - mu) / 3
    s = np.random.normal(mu, sigma, 1)
    return int(s)
    # sns.set_palette("hls") #设置所有图的颜色，使用hls色彩空间
    # sns.distplot(s,color="r",bins=1000,kde=True) #绘制直方图，color设置颜色，bins设置直方图的划分数
    # plt.show() #显示验证结果


# 方法二
def getGaussRandomNum1(min, max):
    mu = (min + max) / 2
    sigma = (max - mu) / 3
    s = random.gauss(mu, sigma)
    return int(s)


print(getGaussRandomNum1(30, 60))