import numpy as np
import matplotlib 
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import pandas as pd
from scipy import interpolate



#读取通过getdata获取的数据点文件
#可通过两种方式绝对地址和相对地址
#file_path = r'D:\sss\python\1420-1.xlsx'
name2=['x','y']
df = pd.read_excel('应力三轴度相关调整.xlsx', usecols='A:B', names=name2 ,index_col=None)

#采用numpy读取excel的数据并存入数组
x1 = np.array([x for x in df['x'].values if str(x) != 'nan'])
y1 = np.array([x for x in df['y'].values if str(x) != 'nan'])

t2 = 1.06
f = interpolate.interp1d(x1,y1,kind='cubic')
z = f(t2)
print(z)

'''
t1 = 200
f1 = interpolate.interp1d(x1,y1,kind='cubic')
z1 = f1(t1)
print(z1)
'''