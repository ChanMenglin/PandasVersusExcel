# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第七课 排序，多重排序
# 2018-10-18

import pandas as pd

products = pd.read_excel('./List.xlsx',index_col='ID')

print('----原始数据----')
print(products)

# sort_values 排序方法
# by：根据什么排序
# inplace：在原数据集中排序，而不是生成新的数据集
# ascending：排序的顺序（True：默认，顺序|False：倒序）

# 以 Price 按 倒序 排序
products.sort_values(by='Price',inplace=True,ascending=False)
print('\n----以 Price 按 倒序 排序----')
print(products)

# 先以 Worthy 按 顺序 排序，再以 Price 按倒序排序
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])
print('\n----先以 Worthy 按 顺序 排序，再以 Price 按倒序排序----')
print(products)