# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第九课 柱状图
# 2018-10-18

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./Students.xlsx')

print('----原始数据----')
print(students)

students.sort_values(by='Number',inplace=True,ascending=False)

# 使用 pandas 绘图（需要使用 matplotlib 展示图表）
# students.plot.bar(x="Field",y='Number',color='orange',title='International Students by Field')

# 使用 matplotlib 绘图
plt.bar(students.Field,students.Number,color='orange')
plt.xticks(students.Field,rotation='90') # 将 Field 旋转 90 度
plt.xlabel('Field') # 设置 x轴 标题
plt.ylabel('Number') # 设置 y轴 标题
plt.title('International Students by Field',fontsize=16) # 设置标题

# 展示图表
plt.tight_layout() # 紧凑型布局
plt.show()