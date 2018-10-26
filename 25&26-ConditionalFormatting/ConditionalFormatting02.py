# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二十六课 条件格式化（下）
# 2018-10-26

import pandas as pd
import seaborn as sns

students = pd.read_excel('./Students.xlsx')
print('----原始数据----')
print(students)
print(students.columns)

# 以下两种效果不要同时使用，会被覆盖

# 根据数据的大小显示不同深度的颜色
col_map = sns.light_palette('green', as_cmap=True)
# students.style.background_gradient(col_map, subset=['Test_1', 'Test_2', 'Test_3'])  # 需要引入 seaborn

# 根据数据的大小显示不同长度的色条
students.style.bar(color='orange', subset=['Test_1', 'Test_2', 'Test_3']) # 不需要引入 seaborn

# 说明
# 由于编辑器的支持问题，此代码的效果可能无法展现
# 请使用 Anaconda 中的 jupyter notebook 中打开 'ConditionalFormatting02.ipynb' 查看运行效果
