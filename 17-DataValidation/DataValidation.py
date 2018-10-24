# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十七课 数据校验，轴的概念
# 2018-10-24

import pandas as pd 

# 方法一
def score_validation(row):
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

# 方法二
def score_validation2(row):
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')

# 在进行数据校验时不要设置 index_col ，这样有助于保证所有数据都进行校验
students = pd.read_excel('./Students.xlsx')
print('----原始数据----')
print(students)
print(students.columns)

print('\n----校验结果----')
students.apply(score_validation,axis=1)

# axis = 1: 横向
# axis = 0: 纵向（默认）