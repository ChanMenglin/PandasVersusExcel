# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十八课 列操作集锦
# 建议在第八讲之后查看
# 2018-10-30

import pandas as pd
import numpy as np

students_001 = pd.read_excel('./Students.xlsx',sheet_name='Page_001')
students_002 = pd.read_excel('./Students.xlsx',sheet_name='Page_002')
print('----原始数据----')
print('\n----Page_001----')
print(students_001)
print('\n----Page_002----')
print(students_002)

# 追加数据集
students_add_dates = pd.concat([students_001,students_002],axis=1)
print('\n----追加数据集(极少使用)----')
print(students_add_dates)

students = pd.concat([students_001,students_002]).reset_index(drop=True)
print('\n----将要使用的数据----')
print(students)

# 追加数据列
# students['Age'] = 25 # 等同于 np.repeat(25,len(students))
students['Age'] = np.arange(0,len(students))
print('\n----追加数据列----')
print(students)

# 删除列
students.drop(columns='Age',inplace=True)
print('\n----删除列----')
print(students)

# 插入列
students.insert(1,column='Foo',value=np.repeat('foo',len(students)))
print('\n----插入列----')
print(students)

# 修改列名
students.rename(columns={'Foo':'FOO','Name':'NAME'},inplace=True)
print('\n----修改列名----')
print(students)

# 删除含空值的行
# 制造空值
students['ID'] = students['ID'].astype(float)
for i in range(3,5):
    students['ID'].at[i] = np.nan

students.dropna(inplace=True)
print('\n----删除含空值的行----')
print(students)


