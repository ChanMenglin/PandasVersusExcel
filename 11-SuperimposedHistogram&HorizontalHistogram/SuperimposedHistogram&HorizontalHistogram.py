# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十一课 绘制分组柱图，深度优化图表
# 2018-10-19

import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('./Users.xlsx',index_col='ID')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total',inplace=True,ascending=True)
print(users)

# stacked: 叠加（默认为False）
users.plot.barh(x='Name',y=['Oct','Nov','Dec'],stacked=True,title='User Behavior')

plt.tight_layout()
plt.show()

# 补充说明
# users.plot.bar(...) 表示制作竖直柱状图
# users.plot.barh(...) 表示制作水平柱状图
# 
# 
# 