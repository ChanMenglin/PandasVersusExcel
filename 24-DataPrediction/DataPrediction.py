# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十四课 线性回归，数据预测
# 2018-10-25

import pandas as pd 
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('./Sales.xlsx',dtype={'Month':str})
print('----原始数据----')
print(sales.head())
print(sales.columns)

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html
# linregress 计算两组测量的线性最小二乘回归。
# 共传递两个参数，这连个参数应为连个数组，并且两个素组的值应该一一对应
# 返回值：
# slope：回归线的斜率
# intercept：回归线的截距
# r：相关系数
# p：假设检验的双侧p值，其零假设是斜率为零，使用Wald检验，检验统计量的t分布
# std_err：估计梯度的标准误差。
slope,intercept,r,p,std_err = linregress(sales.index,sales.Revenue)

# 期望值
exp = sales.index * slope + intercept
# 线性回归方程回归方程
# y = slope * x + intercept

plt.scatter(sales.index,sales.Revenue)
plt.plot(sales.index,exp,color='orange')
plt.title('Sales')
plt.xticks(sales.index,sales.Month,rotation=90)
plt.tight_layout()
plt.show()

