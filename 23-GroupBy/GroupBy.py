# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十三课 透视表，分组，聚合（group by）
# 2018-10-25

import pandas as pd 
import numpy as np

# 设置最大显示列数为20
pd.options.display.max_columns=20
orders = pd.read_excel('./Orders.xlsx')
print('----原始数据----')
print(orders.head())
print(orders.columns)

orders['Year'] = pd.DatetimeIndex(orders['Date']).year

# 方法一
tt1 = orders.pivot_table(index='Category',columns='Year',values='Total',aggfunc=np.sum)
print('\n----方法一----')
print(tt1)

group = orders.groupby(['Category','Year'])
s = group['Total'].sum()
c = group['ID'].count()

tt2 = pd.DataFrame({'Sum':s,'Count':c})
print('\n----方法二----')
print(tt2)