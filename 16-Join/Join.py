# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十六课 多表联合（Join）
# 2018-10-24

import pandas as pd 

students = pd.read_excel('./Student_Score.xlsx',sheet_name='Students',index_col='ID')
scores = pd.read_excel('./Student_Score.xlsx',sheet_name='Scores',index_col='ID')
print('----原始数据----')
print('\n----Students----')
print(students)
print(students.columns)
print('\n----Scores----')
print(scores)
print(scores.columns)

# 联合查询

# 方法一
# how: 链接方式
#   inner(默认)-inner join
#   left-左链接
#   right-右链接
# on: 链接字段(如果省略此属性，merge会自动以相同的列名作为链接的依据，但不会比较 index_col)
# left_on/right_on: 分别指定两张表的链接依据
# fillna(0): 将'NaN'替换为0
table1 = students.merge(scores,how='left',on='ID').fillna(0)
table1.Score = table1.Score.astype(int) # 将Score中的小数转换为整数
print('\n----联合查询 方法一(inner join)----')
print(table1)

# 方法二
# how: 链接方式
#   inner(默认)-inner join
#   left-左链接
#   right-右链接
# on: 链接字段(设置了 index_col 时如果省略此属性，join会自动以 index_col 作为链接的依据)
# fillna(0): 将'NaN'替换为0
table2 = students.join(scores,how='left',on='ID').fillna(0)
table2.Score = table2.Score.astype(int) # 将Score中的小数转换为整数
print('\n----联合查询 方法二(inner join)----')
print(table2)




