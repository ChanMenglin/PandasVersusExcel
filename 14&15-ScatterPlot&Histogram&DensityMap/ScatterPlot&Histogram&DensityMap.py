# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十四课 散点图，直方图，密度图
# 第十五课 密度图，数据相关性
# 2018-10-19

import pandas as pd 
import matplotlib.pyplot as plt

pd.options.display.max_columns = 20
homes = pd.read_excel('./home_data.xlsx',index_col='id')
print('----原始数据----')
print(homes.head())
print(homes.columns)

# 散点图
# homes.plot.scatter(x='sqft_living',y='price')

# 直方图 bins: 分配粒度
# homes.sqft_living.plot.hist(bins=100)
# plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation=90)

# 密度图
homes.sqft_living.plot.kde()
plt.xticks(range(0,max(homes.sqft_living),500),fontsize=8,rotation=90)
plt.show()


