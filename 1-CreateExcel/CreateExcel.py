# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第一课 创建文件
# 2018-10-17

import pandas as pd

df = pd.DataFrame({'ID':[0,1,2],'Name':['Mark','Tomi','Jack']})

# 此处设置数据表的索引，如未设置索引会自动在最前方添加一列作为索引
df = df.set_index('ID') # 会生成新的 DataFrame
# df.set_index('ID',inplace=True) # 在原来的 DataFrame 上进行修改

# 将数据报错到 output.xlsx
df.to_excel('./output.xlsx')

print(df)
print('Done')