import tkinter as tk
import tkinter
from tkinter import messagebox
from tkinter import ttk
from time import sleep
import numpy as np  
import matplotlib 
import matplotlib.pyplot as plt 
import pandas as pd 
import math 
from scipy import interpolate 
import sqlite3 
import os 
import pylab as pl

from matplotlib.backend_bases import key_press_handler
from scipy.interpolate import griddata
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


def main1():
    root1 = tk.Tk()
    root1.title('----')
    root1.geometry('%dx%d+%d+%d'%(850, 700, 300, 100))

#采用numpy读取excel的数据并存入数组
    x1 = [10,20,40,100,200,400,1000,2000,4000,10000,20000,40000,100000,200000,1000000]#,400000
    y1 = [0.0507,0.0357,0.026,0.0177,0.0139,0.011,0.00818,0.00643,0.00518,0.00403,0.00343,0.00293,0.00245,0.00213,0.00163]#,0.00158
    
    x2 = [10,20,40,100,200,400,1000,2000,4000,10000,20000,40000,100000,200000,400000,1000000]
    y2 = [0.0438,0.0318,0.0233,0.0159,0.0125,0.00956,0.00716,0.00581,0.00476,0.00376,0.00316,0.00273,0.00226,0.00196,0.00173,0.00151]

    x3 = [10,20,40,100,200,400,1000,2000,4000,10000,20000,40000,100000,200000,400000,1000000]
    y3 = [0.0378,0.0251,0.0181,0.0123,0.00961,0.00761,0.00571,0.00466,0.00381,0.00301,0.00256,0.00221,0.00182,0.00159,0.00139,0.00118]

    x4 = [10,20,40,100,200,400,1000,2000,4000,10000,20000,40000,100000,200000,400000,1000000]
    y4 = [0.0318,0.0208,0.0148,0.00974,0.00744,0.00574,0.00424,0.00339,0.00279,0.00221,0.00186,0.00161,0.00136,0.00121,0.00109,0.000963]

    x5 = [10,20,40,100,200,400,1000,2000,4000,10000,20000,40000,100000,200000,400000,1000000]
    y5 = [0.0214,0.0149,0.0105,0.00711,0.00551,0.00431,0.00328,0.00268,0.00226,0.00186,0.00162,0.00144,0.00121,0.00108,0.000954,0.000834]


#定义字体字号等参数
    font = {'family':'MicroSoft YaHei', 'weight':'bold','size':'11'}
    matplotlib.rc("font",**font)
            #font1 = {'family' : 'Times New Roman','weight' : 'normal','size'   : 23,}

            #注意此处为第一次贴图并未显示查值点 设置组件容器属性字典集
    sonFrameSetting = {
                    # 设置边框线的宽度
                    'bd': 3,
                    # 设置容器组件的高度
                    'height':360,
                    # 设置组件容器的宽度
                    'width': 420,
                    # 设置组件容器的背景颜色
                    
                    # 设置边框线样式
                    'relief': 'ridge'
                }
                # 创建顶级窗口的组件容器,并传入组件设置
    sonFrame = tk.Frame(root1, sonFrameSetting)
    sonFrame.place(x=0,y=0)
    fig = Figure(figsize=(10,8), dpi=80)
    ax1 = fig.add_subplot(111)

    ax1.set(xlim=[10,1000000],ylim=[0.0001,0.1],)

    ax1.set_xscale('log')
    ax1.set_yscale('log',)
    # ax1.set_yscale('log',basey =2)
    ax1.set_title('蠕变-疲劳损伤包络线',fontsize=12)
    ax1.set_xlabel('Nd',fontsize=12)
    ax1.set_ylabel('应变范围',fontsize=12)
    # ax1.set_xticks([10,10**2,10**3,10**4,10**5,3*10**5,],)
    # ax1.set_yticks([6.9,14,34,69,140,340,690],)
    ax1.tick_params(labelsize=10) #刻度字体大小13
    ax1.grid(True,which="both",ls="-") 
                
    #ax1.plot(x1,y1,color = 'blue')#line1, = 
                #leg1 = ax1.legend(handles=[line1], fontsize=9,loc=[0.8,0.7],frameon=False,handlelength=0)
                #ax1.add_artist(leg1)
    line1, = ax1.plot(x1,y1,color = 'black', label = "100",)
    line2, = ax1.plot(x2,y2,color = 'blue', label = "800",)
    line3, = ax1.plot(x3,y3,color = 'cadetblue', label = "900",)
    line4, = ax1.plot(x4,y4,color = 'gray', label = "1000-1200",)
    line5, = ax1.plot(x5,y5,color = 'darkcyan', label = "1300",)

    t2 = 0.04
    f = interpolate.interp1d(y1,x1,kind='cubic')
    z = f(t2)
    print(z)
    print(t2)

    xnew=np.linspace(0.002,0.05,10000)
    ynew = f(xnew)
    line6, = ax1.plot(ynew,xnew,color = 'gray', label = "new",)

    #line2, = ax1.plot(x2,y2,color = 'black', linestyle='--',label = "2.25Cr-Mo",)
    leg1 = ax1.legend([line1,line2,line3,line4,line5,line6], ["100","800","900","1000-1200","1300","new"], fontsize=9, loc=1)
    ax1.add_artist(leg1)




    ax1.text(0.25,0.75,'计算值坐标：',size =10, color = 'red',)
    ax1.scatter(z,t2,color = 'red',)
    ax1.text(0.5,0.75,'(%.3f, %.3f)' %(z, t2),color ='r',size =10)

# 将绘制的图形显示到tkinter:创建属于root的canvas画布,并将图f置于画布上
    canvas = FigureCanvasTkAgg(fig, master=sonFrame)
    # 注意show方法已经过时了,这里改用draw
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, ) # 上对齐

    # matplotlib的导航工具栏显示上来(默认是不会显示它的)
    toolbar = NavigationToolbar2Tk(canvas, sonFrame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, ) # get_tk_widget()得到的就是_tkcanvas


    root1.mainloop()

main1()

            