# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十二课 读取CSV、TSV、TXT文件中的数据
# 2018-10-25

import pandas as pd 

student_csv = pd.read_csv('./Students.csv',index_col='ID')
print('----读取 csv 数据----')
print(student_csv)

# sep 指定分隔符（读取csv文件时可省略，默认为 ','）
student_tsv = pd.read_csv('./Students.tsv',sep='\t',index_col='ID')
print('\n----读取 tsv 数据----')
print(student_tsv)

student_txt = pd.read_csv('./Students.txt',sep='|',index_col='ID')
print('\n----读取 txt 数据----')
print(student_txt)