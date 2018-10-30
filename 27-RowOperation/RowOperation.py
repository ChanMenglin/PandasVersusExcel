# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十七课 行操作集锦
# 建议在第八讲之后查看
# 2018-10-30

import pandas as pd 

students_001 = pd.read_excel('./Students.xlsx',sheet_name='Page_001',index_col='ID')
students_002 = pd.read_excel('./Students.xlsx',sheet_name='Page_002',index_col='ID')
print('----原始数据----')
print('\n----Page_001----')
print(students_001)
print('\n----Page_002----')
print(students_002)

# 追加数据集
students_add_dates = students_001.append(students_002)
print('\n----追加数据集----')
print(students_add_dates)

# 追加数据行
stu_col1 = pd.Series({'Name':'Abel','Score':99})
students_add_col = students_add_dates.append(stu_col1,ignore_index=True)
print('\n----追加数据行----')
print(students_add_col)

# 更改数据
students_001.at[1,'Name'] = 'Jack'
students_001.at[1,'Score'] = 100
print('\n----更改数据 方法一----')
print(students_001)

stu_col2 = pd.Series({'ID':1,"Name":'Chen','Score':110})
students_001.iloc[0] = stu_col2 # iloc 的参数为行数 ，从0开始
print('\n----更改数据 方法二----')
print(students_001)

# 在数据中插入一行
stu_col3 = pd.Series({"Name":'Scort','Score':110})
part1 = students_001[:15]
part2 = students_001[15:]
students_001 = part1.append(stu_col3,ignore_index=True).append(part2,ignore_index=True)
print('\n----在数据中插入一行----')
print(students_001)

# 删除数据行
students_drop_col = students_001.drop(index=[15])
print('\n----删除数据行----')
print(students_drop_col)

# 带条件的删除
# 设置空值
for i in range(5, 15):
    students_001['Name'].at[i] = ''

# 去掉空值
missing = students_001.loc[students_001['Name'] == '']
students_001.drop(missing.index, inplace=True)
print('\n----带条件的删除----')
print(students_001)