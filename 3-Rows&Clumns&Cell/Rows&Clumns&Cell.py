# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第三课 行、列、单元格
# 2018-10-17

import pandas as pd

# --创建Series--

# 方法一
d = {'X':100,'Y':200,'Z':300}
s1 = pd.Series(d) # 序列对象
s1.name
s1.index
print(s1.index)

# 方法二
L1 = [100,200,300]
L2 = ['X','Y','Z']
s2 = pd.Series(L1,index=L2)
print(s2.index)

# --操作Excel--

s1 = pd.Series([1,2,3],index=[1,2,3],name='A')
s2 = pd.Series([10,20,30],index=[1,2,3],name='B')
s3 = pd.Series([100,200,300],index=[1,2,3],name='C')

df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
print(df)