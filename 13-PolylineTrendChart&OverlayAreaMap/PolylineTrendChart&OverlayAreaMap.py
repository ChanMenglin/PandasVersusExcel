# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十三课 绘制折线趋势图、叠加区域图
# 2018-10-19

import pandas as pd 
import matplotlib.pyplot as plt

weeks = pd.read_excel('./Orders.xlsx',index_col='Week')
print('----原始数据----')
print(weeks)

# 叠加区域图
weeks.plot.area(y=['Accessories','Bikes','Clothing','Components'])
# 叠加柱状图
# weeks.plot.bar(y=['Accessories','Bikes','Clothing','Components'],stacked=True)
plt.title('Sales Weekly Trend',fontsize=16,fontweight='bold')
plt.ylabel('Total',fontsize=12,fontweight='bold')
plt.xticks(weeks.index,fontsize=8)
plt.show()

# 补充说明
# weeks.plot(...) 绘制折线图
# weeks.plot.area(...) 绘制叠加区域图
# weeks.plot.bar(...) 绘制叠加柱状腿
# 