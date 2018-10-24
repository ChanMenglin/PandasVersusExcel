# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十课 定位、消除重复数据
# 2018-10-24

import pandas as pd 

students = pd.read_excel('./Students_Duplicates.xlsx')
print('----原始数据----')
print(students)
print(students.columns)

dupe = students.duplicated(subset='Name')
print('\n----检查重复数据（True为重复）----')
print(dupe)

dupe = dupe[dupe] # 获取重复的行，等同于dupe = dupe[dupe==True]
print('\n----查看重复数据----')
print(students.iloc[dupe.index])

students.drop_duplicates(subset='Name',inplace=True)
print('\n----消除重复数据后的数据----')
print(students)
