# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十二课 绘制饼图
# 2018-10-19

import pandas as pd 
import matplotlib.pyplot as plt

students = pd.read_excel('./Students.xlsx',index_col="From")
print('----原始数据----')
print(students)

# counterclock: True(默认值): 逆时针，False: 顺时针
students['2017'].plot.pie(fontsize=8,counterclock=False)
plt.title('Source of International Students',fontsize=16,fontweight='bold')
plt.ylabel('2017',fontsize=12,fontweight='bold')
plt.show()