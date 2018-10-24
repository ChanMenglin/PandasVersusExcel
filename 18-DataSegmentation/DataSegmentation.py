# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第十八课 把一列数据分割成两列
# 2018-10-24

import pandas as pd 

employees = pd.read_excel('./Employees.xlsx',index_col='ID')
df = employees['Full Name'].str.split(expand=True)
print('----原始数据----')
print(employees)
print(employees.columns)
print(df)

employees['First Name'] = df[0]
employees['Last Name'] = df[0]
print('\n----分割后的结果----')
print(employees)

# 补充
# split() 方法：
# split(' ',n=0,expand=True)
# split 的第一个参数： 表示分隔符默认为空格或tab
# split 的第二个参数 n： 表示最多分割的个数（0或-1 表示分割成尽可能多的个数）
# split 的第二个参数 expand： 默认为 False （False：分割后生成数组，占一列；True： 分割成单独的列）