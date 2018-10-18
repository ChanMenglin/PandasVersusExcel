# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第六课 函数填充
# 2018-10-18

import pandas as pd

books = pd.read_excel('./Books.xlsx',index_col='ID')
print('----计算前----')
print(books)

# 方法一

# books['Price'] = books['ListPrice'] * books['Discount']
# print('----方法一----')
# print(books)

# 方法二（此方法可以对计算的行的范围进行精确控制）

for i in range(5,16): # books.index:
    books['Price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]
print('----方法二----')
print(books)

# 方法一
books['ListPrice'] += 2

# 方法二
def add_2(x):
    return x + 2
books['ListPrice'] = books['ListPrice'].apply(add_2)

# 方法三
books['ListPrice'] = books['ListPrice'].apply(lambda x:x+2)
print(books)