import tkinter
from tkinter import*
import numpy as np
import matplotlib 
import tkinter as tk
from tkinter import Label, messagebox,filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from docx.enum.text import WD_ALIGN_PARAGRAPH
import math
import os
#from os import write
import docx
import xlwt
import pandas as pd
from scipy import interpolate
import matplotlib.pyplot as plt 
import pylab as pl
from docx.shared import Pt,RGBColor #字号，颜色
from docx.oxml.ns import qn #设置中文字体需要该模块

#读取通过getdata获取的数据点文件
#可通过两种方式绝对地址和相对地址
#file_path = r'D:\sss\python\1420-1.xlsx'
name2=['x','y']
df = pd.read_excel('1420-1.xlsx', usecols='A:B', names=name2 ,index_col=None)

#采用numpy读取excel的数据并存入数组
x1 = np.array([x for x in df['x'].values if str(x) != 'nan'])
y1 = np.array([x for x in df['y'].values if str(x) != 'nan'])

t2 = 0.01
f = interpolate.interp1d(y1,x1,kind='cubic')
z = f(t2)
print(t2)
print(z)

t3 = 20
fzx = interpolate.interp1d(x1,y1,kind='cubic')
z1 = fzx(t3)
print(t3)
print(z1)

'''
t1 = 200
f1 = interpolate.interp1d(x1,y1,kind='cubic')
z1 = f1(t1)
print(t1,z1)'''