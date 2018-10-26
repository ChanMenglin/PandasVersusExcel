# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十五课 条件格式化（上）
# 2018-10-26

import pandas as pd
import seaborn as sns


def low_score_red(s):
    color = 'red' if s < 60 else 'black'
    return f'color:{color}'


def highest_score_green(col):
    return ['background-color:lime' if s == col.max() else 'background-color:white' for s in col]


students = pd.read_excel('./Students.xlsx')
print('----原始数据----')
print(students)
print(students.columns)

students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3']) \
    .apply(highest_score_green, subset=['Test_1', 'Test_2', 'Test_3'])

# 说明
# 由于编辑器的支持问题，此代码的效果可能无法展现
# 请使用 Anaconda 中的 jupyter notebook 中打开 'ConditionalFormatting01.ipynb' 查看运行效果


