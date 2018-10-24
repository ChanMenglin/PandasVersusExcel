# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十九课 求和，求平均，统计导引
# 2018-10-24

import pandas as pd 

students = pd.read_excel('./Students.xlsx',index_col='ID')
print('----原始数据----')
print(students)
print(students.columns)

temp = students[['Test_1','Test_2','Test_3']]
print('\n----需要计算的元数据----')
print(temp)

# 和
raw_sum = temp.sum(axis=1)
print('\n----求和----')
print(raw_sum)

# 平均值
raw_mean = temp.mean(axis=1)
print('\n----求平均值----')
print(raw_mean)

students['Total'] = raw_sum
students['Average'] = raw_mean
print('\n----整合结果----')
print(students)

col_mean = students[['Test_1','Test_2','Test_3','Total','Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean,ignore_index=True)
print('\n----最终结果----')
print(students)

# axis = 1: 横向
# axis = 0: 纵向（默认）