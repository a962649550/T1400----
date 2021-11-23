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

lstt1 = [0,0,0,0,0,0,0,0,0,0,0,0]
#定义字体字号等参数
font = {'family':'MicroSoft YaHei', 'weight':'bold','size':'11'}
matplotlib.rc("font",**font)
font1 = {'family' : 'Times New Roman','weight' : 'normal','size'   : 23,}
#读取通过getdata获取的数据点文件
#可通过两种方式绝对地址和相对地址
#file_path = r'D:\sss\python\1420-1.xlsx'
name2=['100x','100y','800x','800y','900x','900y','1100x','1100y','1300x','1300y']
df = pd.read_excel('T1420-1B.xlsx', usecols='A:J', names=name2 ,index_col=None)
#name2=['100x','100y','800x','800y','900x','900y','1100x','1100y','1300x','1300y']
#df = pd.read_excel('应力三轴度相关调整.xlsx', usecols='A:J', names=name2 ,index_col=None)

#采用numpy读取excel的数据并存入数组
x1 = np.array([x for x in df['100x'].values if str(x) != 'nan'])
y1 = np.array([x for x in df['100y'].values if str(x) != 'nan'])
x2 = np.array([x for x in df['800x'].values if str(x) != 'nan'])
y2 = np.array([x for x in df['800y'].values if str(x) != 'nan'])
x3 = np.array([x for x in df['900x'].values if str(x) != 'nan'])
y3 = np.array([x for x in df['900y'].values if str(x) != 'nan'])
x4 = np.array([x for x in df['1100x'].values if str(x) != 'nan'])
y4 = np.array([x for x in df['1100y'].values if str(x) != 'nan'])
x5 = np.array([x for x in df['1300x'].values if str(x) != 'nan'])
y5 = np.array([x for x in df['1300y'].values if str(x) != 'nan'])

def main1():
    root1 = tk.Tk()
    root1.title('----')
    root1.geometry('%dx%d+%d+%d'%(800, 600, 300, 100))

    #定义界面按钮及标签
    #labelName = tk.Label(root1,text = '设计疲劳曲线：', anchor = "w", font = ("宋体",18),fg = 'blue')
    #labelName.place(x=25, y=20, width=220, height=30)

    #labelPwd = tk.Label(root1,text = '应力幅值 Sa(MPa):', anchor = "w", font = ("宋体",12),fg = 'purple')
    #labelPwd.place(x=40, y=70, width=200, height=30)

    varPwd = tk.StringVar(root1, value='')
    entryPwd = tk.Entry(root1,  textvariable = varPwd, font = ("宋体",12),fg = 'purple')
    entryPwd.place(x = 45, y = 100, width = 100,height = 33)

    #labelJieguo = tk.Label(root1,text = '允许循环次数:',width=80, anchor = "w", font = ("宋体",12),fg = 'purple')
    #labelJieguo.place(x=40, y=190, width=200, height=30)

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
    sonFrame.place(x=270,y=90)

    fig = Figure(figsize=(5,4), dpi=90)
    ax1 = fig.add_subplot(111)

    ax1.set(xlim=[10,1000000],ylim=[0.0001,0.1],)

    ax1.set_xscale('log')
    ax1.set_yscale('log',)
    # ax1.set_yscale('log',basey =2)
    ax1.set_title('图1',fontsize=10)
    ax1.set_xlabel('允许循环次数 Nd',fontsize=8)
    ax1.set_ylabel('应变范围',fontsize=8)
    # ax1.set_xticks([10,10**2,10**3,10**4,10**5,3*10**5,],)
    # ax1.set_yticks([6.9,14,34,69,140,340,690],)
    ax1.tick_params(labelsize=10) #刻度字体大小13
    ax1.grid(True,which="both",ls="-") 
                
    #ax1.plot(x1,y1,color = 'blue')#line1, = 
                #leg1 = ax1.legend(handles=[line1], fontsize=9,loc=[0.8,0.7],frameon=False,handlelength=0)
                #ax1.add_artist(leg1)
    line1, = ax1.plot(x1,y1,color = 'silver', label = "427",)
    line2, = ax1.plot(x2,y2,color = 'blue', label = "454",)
    line3, = ax1.plot(x3,y3,color = 'cadetblue', label = "482",)
    line4, = ax1.plot(x4,y4,color = 'gray', label = "510",)
    line5, = ax1.plot(x5,y5,color = 'darkcyan', label = "538",)
                #ax1.text(40000,525,'Temperature,℃',size =10)
    '''ax1.text(18,170,'计算值坐标：',size =10, color = 'red',)
    ax1.scatter(z,t2,color = 'red',)
    ax1.text(18,130,'(%s , %.4f)' %(t2, z),color ='r',size =10)'''

                # 将绘制的图形显示到tkinter:创建属于root的canvas画布,并将图f置于画布上
    canvas = FigureCanvasTkAgg(fig, master=sonFrame)
    # 注意show方法已经过时了,这里改用draw
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, ) # 上对齐

    # matplotlib的导航工具栏显示上来(默认是不会显示它的)
    toolbar = NavigationToolbar2Tk(canvas, sonFrame)
    toolbar.update()
    canvas._tkcanvas.pack(side=tk.TOP, ) # get_tk_widget()得到的就是_tkcanvas
    global pp2
    pp2 = 0
    lst2=[]
    def login():
        
        #text.config(state = 'normal')
        #text.delete('1.0','end')

        #y0 = entryName.get() #时间
        x0 = entryPwd.get()

        #判定输入值是否非空
        if x0 == "":
            tk.messagebox.showwarning("警告","请输入应力幅值后,再点击应用")
        elif x0 != "":
            t2 = float(entryPwd.get())
            global varheightfasteningstressCT
            varheightfasteningstressCT = t2

            if t2 <0.0001 or t2 >0.1:
                tk.messagebox.showwarning("警告","输入数据超出图示范围")
                #varPwd.set('')
                #text.config(state = 'normal')
                #text.delete('1.0','end')
            elif t2>=0.0001 and t2 <=0.1:
                f = interpolate.interp1d(y1,x1,kind='cubic')
                z = f(t2)

                #text.insert('insert',int(z))
                #text.config(state = 'disabled')
                global varheightfasteningstressCSr
                varheightfasteningstressCSr = z

                # 设置组件容器属性字典集
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
                sonFrame.place(x=270,y=90)

                fig = Figure(figsize=(5,4), dpi=90)
                ax1 = fig.add_subplot(111)

                ax1.set(xlim=[10,1000000],ylim=[0.0001,0.1],)

                ax1.set_xscale('log')
                ax1.set_yscale('log',)
                # ax1.set_yscale('log',basey =2)
                ax1.set_title('图1',fontsize=10)
                ax1.set_xlabel('允许循环次数 Nd',fontsize=8)
                ax1.set_ylabel('应变范围',fontsize=8)
                # ax1.set_xticks([10,10**2,10**3,10**4,10**5,3*10**5,],)
                # ax1.set_yticks([6.9,14,34,69,140,340,690],)
                ax1.tick_params(labelsize=10) #刻度字体大小13
                ax1.grid(True,which="both",ls="-") 
                
                ax1.plot(x1,y1,color = 'blue')#line1, = 
                #leg1 = ax1.legend(handles=[line1], fontsize=9,loc=[0.8,0.7],frameon=False,handlelength=0)
                #ax1.add_artist(leg1)
                
                #ax1.text(40000,525,'Temperature,℃',size =10)
                #定义结果并格式化后再图层上显示出来
                ax1.text(18,170,'计算值坐标：',size =10, color = 'red',)
                ax1.scatter(z,t2,color = 'red',)
                ax1.text(18,0.0009,'(%s , %.4f)' %(t2, z),color ='r',size =10)

                # 将绘制的图形显示到tkinter:创建属于root的canvas画布,并将图f置于画布上
                canvas = FigureCanvasTkAgg(fig, master=sonFrame)
                # 注意show方法已经过时了,这里改用draw
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, ) # 上对齐

                # matplotlib的导航工具栏显示上来(默认是不会显示它的)
                toolbar = NavigationToolbar2Tk(canvas, sonFrame)
                toolbar.update()
                canvas._tkcanvas.pack(side=tk.TOP, ) # get_tk_widget()得到的就是_tkcanvas

                '''def on_key_event(event):
                    """键盘事件处理"""
                    print("你按了%s" % event.key)
                    key_press_handler(event, canvas, toolbar)
                
                canvas.mpl_connect('key_press_event', on_key_event)'''
                #将疲劳分析的结果存入列表2中，用于当前界面即时显示工况结果
                lst2.append(int(z))

                global pp2
                pp2 +=1
                text.insert(tk.INSERT,str(lst2[pp2-1])+'\n')
                #text.insert(tk.INSERT,'工况'+str(pp2)+'-'+str(t2)+'MPa'+': '+str(lst2[pp2-1])+'\n')
                #将结果放入最终评定的列表
                lstt1[pp2-1] = int(z)
                print(lstt1)

    buttonOk = tk.Button(root1,text='计算',command=login, font = ("宋体",12),fg = 'purple')
    buttonOk.place(x=60, y =500, width=60, height=30)

    
    #定义帮助按钮及其界面
    def cancel():
        helpwindow2 = tk.Toplevel()
        helpwindow2.title('帮助')
        helpwindow2.geometry('550x400+600+100')
        labelhelp1 = tk.Label(helpwindow2,text = '说明:' ,width=80, anchor = "w", font = ("宋体",12), fg = "blue")
        labelhelp1.place(x=25, y=20, width=220, height=30)

        labelhelp2 = tk.Label(helpwindow2,text = '1.输入应力循环幅值,点击应用可在右侧的设计疲劳曲线图',width=80, anchor = "w", font = ("宋体",12),fg = 'purple')
        labelhelp2.place(x=60, y=50, width=420, height=30)

        labelhelp2 = tk.Label(helpwindow2,text = '  绘出所求点的位置以及数据值.',width=80, anchor = "w", font = ("宋体",12),fg = 'purple')
        labelhelp2.place(x=60, y=80, width=420, height=30)

        labelhelp7 = tk.Label(helpwindow2,text = '2.请按工况顺序输入参数,系统会顺序保存结果用于综合评定.',width=80, anchor = "w", font = ("宋体",12),fg = 'purple')
        labelhelp7.place(x=60, y=110, width=450, height=30)

        labelhelp3 = tk.Label(helpwindow2,text = '注意:',width=80, anchor = "w", font = ("宋体",12),fg = "blue")
        labelhelp3.place(x=25, y=140, width=220, height=30)

        labelhelp4 = tk.Label(helpwindow2,text = '1.填写数据的单位要一致,不可输入非数字影响计算.',width=80, anchor = "w", font = ("宋体",12),)
        labelhelp4.place(x=60, y=170, width=400, height=30)

        labelhelp5 = tk.Label(helpwindow2,text = '2.适用范围:应力幅值区间为276到2353,最大循环次数为100000 .',width=80, anchor = "w", font = ("宋体",12),)
        labelhelp5.place(x=60, y=200, width=450, height=30)

        labelhelp6 = tk.Label(helpwindow2,text = '3.此图为GB/T 34019-2017图1 .',width=80, anchor = "w", font = ("宋体",12),)
        labelhelp6.place(x=60, y=230, width=420, height=30)
        helpwindow2.mainloop()
        #清除用户输入的用户名
        #varName.set('')
        #varPwd.set('')
        #text.config(state = 'normal')
        #text.delete('1.0','end')
        
    #buttonCancel = tk.Button(root1,text='帮助',command=cancel, font = ("宋体",12),fg = 'purple')
    #buttonCancel.place(x=190, y =500, width=60, height=30)

    '''def nextstep():
        root1.destroy()
        # Averagestress_Clicka()

    buttonnextstep = tk.Button(root1,text='退出',command=nextstep, font = ("宋体",12),fg = 'purple')
    buttonnextstep.place(x = 580, y = 500, width = 60, height = 30)'''

    #定义texe文本显示框
    text = tk.Text(root1,width=11,height=3, font = ("宋体",12),fg = 'purple')
    text.place(x=45, y=220)
    #text.insert(tk.INSERT,'工况'+str(pp2)+'-'+str(t2)+'MPa'+':'+str(lst2[pp2-1])+'\n')

    #定义滚动条
    scroll = tkinter.Scrollbar()
    scroll.place(x = 220,y = 220,width=20,height =140)
    scroll.config(command=text.yview)
    text.config(yscrollcommand=scroll.set)
    #labeldanwei = tk.Label(root1,text = '( MPa )', anchor = "w", font = ("宋体",12),fg = 'purple')
    #labeldanwei.place(x=436, y=110, width=220, height=30)

    #定义上一步按钮，点击后关闭疲劳分析界面打开断裂力学法界面
    def laststep():
        root1.destroy()


    #定义下一步按钮，点击后关闭疲劳分析界面打开综合评定界面
    def help1():
        root1.destroy()


    def closewindow():
        root1.destroy()

    #定义界面按钮
    #buttonlaststep = tk.Button(root1,text='上一步',command=laststep, font = ("宋体",12),fg = 'purple')
    #buttonlaststep.place(x=320, y =500, width=60, height=30)
    #button5 = tk.Button(root1, text='下一步', font = ("宋体",13),fg = 'purple', command=help1)
    #button5.place(x=450, y =500, width=60, height=30)
    #按钮放置位置：x = 620, y = 500, width = 60, height = 35
    root1.mainloop()

main1()


'''
#读取通过getdata获取的数据点文件
#可通过两种方式绝对地址和相对地址
#file_path = r'D:\sss\python\1420-1.xlsx'
name2=['x','y']
df = pd.read_excel('1420-1.xlsx', usecols='A:B', names=name2 ,index_col=None)

#采用numpy读取excel的数据并存入数组
x1 = np.array([x for x in df['x'].values if str(x) != 'nan'])
y1 = np.array([x for x in df['y'].values if str(x) != 'nan'])

t2 = 0.02
f = interpolate.interp1d(y1,x1,kind='cubic')
z = f(t2)
print(z)

t1 = 200
f1 = interpolate.interp1d(x1,y1,kind='cubic')
z1 = f1(t1)
print(z1)


#定义全局变量
varheightfasteningstressCtime = 0
varheightfasteningstressCT = 0
varheightfasteningstressCSr = 0
sum1 = 0
ac = 0
lstgongkuang = ['','','','','','','','','','']

lstt1 = ['','','','','','','','','','']
lstt2 = ['','','','','','','','','','']
#lstt2 = [0,0,0,0,0,0,0,0,0,0]
'''