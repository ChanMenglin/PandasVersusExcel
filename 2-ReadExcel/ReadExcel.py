# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第二课 读取文件
# 2018-10-17

import pandas as pd

# --基本数据的读取--

# 读取文件
# head：默认0，表示开始读取的行（默认会跳过顶部的空行）
# index_col: 指定数据的索引列
people = pd.read_excel('./People.xlsx',head=1,index_col='ID')
# 读取文件的行数和列数
shape = people.shape
# 读取文件的行,不会显示索引列
columns = people.columns
# 读取文件的前几行（默认为5，可传入指定行数）
head = people.head()
# 读取文件的末尾几行（默认为5，可传入指定行数）
tail = people.tail()

# --当数据文件存在坏数据时可按以下方式处理--
# （以下内容根据实际情况使用，同时使用会造成数据混乱）

# 当标题行上有坏数据时可使用 head 参数
people1 = pd.read_excel('./People.xlsx',head=1)

# 当数据表中没有标题行时可将 head 的值设为 None 表示无标题
people2 = pd.read_excel('./People.xlsx',head=None)
people2.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']

print(columns)