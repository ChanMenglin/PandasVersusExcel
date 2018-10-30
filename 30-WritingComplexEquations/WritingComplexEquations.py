# pandasVersusExcel
# http://sa.mentorx.net/course/89/tasks
# 第三十课 编写复杂方程
# 建议在第八讲之后查看
# 2018-10-30

import pandas as pd
import numpy as np

# 计算外接圆的面积
def get_Circumscribedcircle_area(lengh,height):
    r = np.sqrt(lengh**2 + height**2) / 2
    return r**2*np.pi

def wrapper(row):
    return get_Circumscribedcircle_area(row['Length'],row['Height'])
    

rectangles = pd.read_excel('./Rectangles.xlsx',index_col='ID')
print('----原始数据----')
print(rectangles)

rectangles['CA'] = rectangles.apply(lambda row: get_Circumscribedcircle_area(row['Length'],row['Height']),axis=1)
# rectangles['CA'] = rectangles.apply(wrapper,axis=1)
print(rectangles)
