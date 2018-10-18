# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十课 绘制分组柱图，深度优化图表
# 2018-10-18

import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('./Students.xlsx')

print('----原始数据----')
print(students)

students.sort_values(by='2017',inplace=True,ascending=False)
students.plot.bar(x='Field',y=['2016','2017'],color=['orange','red'])

plt.title('International Students by Field',fontsize=16,fontweight='bold')
plt.xlabel('Field',fontweight='bold')
plt.ylabel('Numbers',fontweight='bold')
ax = plt.gca() # 获取图表的轴
ax.set_xticklabels(students['Field'],rotation=45,ha='right')
f = plt.gcf() # 获取图表的图形
f.subplots_adjust(left=0.2,bottom=0.42)
# plt.tight_layout()
plt.show()