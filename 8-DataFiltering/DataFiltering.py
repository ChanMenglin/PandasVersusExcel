# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第八课 数据筛选、过滤
# 2018-10-18

import pandas as pd

Students = pd.read_excel('./Students.xlsx',index_col='ID')

print('----原始数据----')
print(Students)

# Age 大于等于 18 小于 30
def age_18_to_30(age):
    return 18 <= age < 30

# 成绩在 85 到 100 之间
def level_a(score):
    return 85 <= score <= 100

# 筛选 Age 大于等于 18 小于 30 的学生
Students = Students.loc[Students['Age'].apply(lambda age:18 <= age < 30)]
print('\n----筛选 Age 大于等于 18 小于 30 的学生----')
print(Students)

# 筛选 Age 大于等于 18 小于 30 成绩在 85 到 100 之间 的学生
Students = Students.loc[Students.Age.apply(age_18_to_30)] \
    .loc[Students.Score.apply(level_a)]
print('\n----筛选 Age 大于等于 18 小于 30 成绩在 85 到 100 之间 的学生----')
print(Students)

# 补充知识点
# 1. Students['Age'] 的写法可以简写为 Students.Age
# 2. age_18_to_30 函数可以用 lambda 表达式代替，因此
#    .apply(age_18_to_30) 可以简写为 .apply(lambda age:18 <= age < 30)
# 3. Python 中 如遇表达式过长可以使用 ' \'(空格加正斜杠加回车)的方式换行
