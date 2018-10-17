# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第四课 数据区域的读取，填充整数、文字
# 第五课 填充日期序列
# 2018-10-17

import pandas as pd
from datetime import date,timedelta

# --数据区域的读取--

# skiprows: 从序号为3的行开始读取(类似于 header)
# usecols： 读取列的范围
# dtype: 设置每一列的数据类型
books = pd.read_excel('./Books.xlsx',skiprows=3,usecols='C:F',dtype={'ID':str,'Name':str,'InStore':str,'Date':str})
print(books)


print('-----------------分隔符-----------------')

# --填充整数、文字、日前--

# 日期加月份
# d：起始日期，type：date
# month_delta： 要添加的月数，type：int
# 返回添加后的结果，type：date
def add_month(d, month_delta):
    year_delta = month_delta // 12
    month = d.month + month_delta % 12
    if month != 12:
        year_delta += month // 12
        month = month % 12
    return date(d.year + year_delta, month, d.day)

start = date(2018,10,17)

for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    books['Date'].at[i] = start + timedelta(days=i)
print(books)

books.set_index('ID')
books.to_excel('./Books_output.xlsx')
print('-----------------Done-----------------')
