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




#x=np.linspace(0,10,11)
x=[0,0.3,1]
y=[1,0.3,0]
#y=np.sin(x)
x1=np.linspace(0,1,101)
f = interpolate.interp1d(x,y,kind = 'slinear')
y1 = f(x1)

def supportingunelasticB2c():


    textFont1 = ("宋体", 14,"bold" )


    class LabelWidget(tkinter.Entry):
        def __init__(self, master, x, y, text):
            self.text = tkinter.StringVar()
            self.text.set(text)
            tkinter.Entry.__init__(self, master=master)
            self.config(relief="ridge", font=textFont1,
                        bg="black", fg="black",
                        readonlybackground="#ddddddddd",
                        justify='center',width=6,
                        textvariable=self.text,
                        state="readonly")
            self.grid(column=x, row=y)

    class EntryWidget(tkinter.Entry):
        def __init__(self, master, x, y):
            tkinter.Entry.__init__(self, master=master)
            self.value = tkinter.StringVar()
            self.config(textvariable=self.value, width=6,
                        relief="ridge", font=textFont1,
                        bg="white", fg="#000000000",
                        justify='center')
            self.grid(column=x, row=y)
            self.value.set("")

    class EntryGrid(tkinter.Toplevel):
        ''' Dialog box with Entry widgets arranged in columns and rows.'''
        def __init__(self, colList, rowList, title="蠕变-疲劳评定"):
            tkinter.Toplevel.__init__(self)
            self.cols = colList[:]
            self.colList = colList[:]
            self.colList.insert(0, "序号")
            self.rowList = rowList
            self.title(title)
            self.geometry("1160x720+80+60")

            
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
            sonFrame = tk.Frame(self, sonFrameSetting)
            sonFrame.place(x=670,y=290)

            fig = Figure(figsize=(5,4), dpi=80)
            ax1 = fig.add_subplot(111)

            ax1.set(xlim=[0,1],ylim=[0,1],)

            #ax1.set_xscale('log')
            #ax1.set_yscale('log',)
    # ax1.set_yscale('log',basey =2)
            ax1.set_title('蠕变-疲劳损伤包络线',fontsize=12)
            #ax1.set_xlabel('11',fontsize=12)
            #ax1.set_ylabel('22',fontsize=12)
    # ax1.set_xticks([10,10**2,10**3,10**4,10**5,3*10**5,],)
    # ax1.set_yticks([6.9,14,34,69,140,340,690],)
            ax1.tick_params(labelsize=10) #刻度字体大小13
            ax1.grid(True,which="both",ls="-") 
                
    #ax1.plot(x1,y1,color = 'blue')#line1, = 
                #leg1 = ax1.legend(handles=[line1], fontsize=9,loc=[0.8,0.7],frameon=False,handlelength=0)
                #ax1.add_artist(leg1)
            line1, = ax1.plot(x1,y1,color = 'black', label = "427",)
    #line2, = ax1.plot(x2,y2,color = 'blue', label = "454",)
    #line3, = ax1.plot(x3,y3,color = 'cadetblue', label = "482",)
    #line4, = ax1.plot(x4,y4,color = 'gray', label = "510",)
    #line5, = ax1.plot(x5,y5,color = 'darkcyan', label = "538",)
                #ax1.text(40000,525,'Temperature,℃',size =10)

            '''z = 0.5
            t2 = 0.3

            ax1.text(0.25,0.75,'计算值坐标：',size =10, color = 'red',)
            ax1.scatter(z,t2,color = 'red',)
            ax1.text(0.5,0.75,'(%.3f, %.3f)' %(z, t2),color ='r',size =10)'''

                # 将绘制的图形显示到tkinter:创建属于root的canvas画布,并将图f置于画布上
            canvas = FigureCanvasTkAgg(fig, master=sonFrame)
    # 注意show方法已经过时了,这里改用draw
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, ) # 上对齐
            


            self.labelOverallPrimaryFilmStress = tkinter.Label(self,text='请输入各个载荷-温度-时间段的相关参数:',anchor = "w", font = ("宋体",12),fg = "purple")
            self.labelOverallPrimaryFilmStress.place(x = 35, y = 20, width = 440,height = 30)

            self.labelOverallPrimaryFilmStress = tkinter.Label(self,text='请选择校核材料类型:',anchor = "w", font = ("宋体",12),fg = "purple")
            self.labelOverallPrimaryFilmStress.place(x = 30, y = 290, width = 240,height = 30)

            self.xvariable = tkinter.StringVar()
            self.combobox = ttk.Combobox(self, textvariable = self.xvariable)
            self.combobox.place(x = 225, y = 290, width = 160, height = 30)
            self.combobox["value"] = ( "", "默认1", "默认2")
            self.combobox.current(0)
            def xFunc(event):
                print(self.combobox.get())
                self.cailiao = self.combobox.get()
            # print(self.cailiao)

            self.combobox.bind("<<ComboboxSelected>>", xFunc)


            self.labelResult = tkinter.Label(self,text='疲劳损伤:',anchor = "w", font = ("宋体",12),fg = "red")
            self.labelResult.place(x = 30, y = 340, width = 160, height = 30)

            self.labelResult = tkinter.Label(self,text='蠕变损伤:',anchor = "w", font = ("宋体",12),fg = "red")
            self.labelResult.place(x = 320, y = 340, width = 160, height = 30)

            self.labelhelp1 = tkinter.Label(self,text='使用步骤:',anchor = "w", font = ("宋体",12), fg = "blue")
            self.labelhelp1.place(x = 30, y = 400, width = 160, height = 30)

            self.labelhelp2 = tkinter.Label(self,text=' PL：薄膜应力(MPa)； QR：所考虑循环中二次应力强度的最大范围；',anchor = "w", font = ("宋体",12),fg = "lightseagreen")
            self.labelhelp2.place(x = 50, y = 430, width = 600, height = 30)

            self.labelhelp2 = tkinter.Label(self,text=' Pb：弯曲应力(MPa)； Kt：蠕变效应引起的外层纤维减小系数；',anchor = "w", font = ("宋体",12),fg = "lightseagreen")
            self.labelhelp2.place(x = 50, y = 470, width = 600, height = 30)
            

            self.labelhelp3 = tkinter.Label(self,text=' SyL：对应QR的应力极限相应的沿壁厚平均温度中的较小值(MPa)；',anchor = "w", font = ("宋体",12),fg = "lightseagreen")
            self.labelhelp3.place(x = 50, y = 510, width = 600, height = 30)

            self.labelhelp4 = tkinter.Label(self,text=' time：工作时间(h/小时)； T：为工作温度(℃)；   ',anchor = "w", font = ("宋体",12),fg = "lightseagreen")
            self.labelhelp4.place(x = 50, y = 550, width = 600, height = 30)

            #self.labelhelp2 = tkinter.Label(self,text='各载荷-温度-时间段的参数输入完整后，选择校核材料的类型，母材限制为1%；焊缝金属应变限制在0.5%，最后点击校核会在输出框输出计算结果。',anchor = "w", font = ("宋体",12),fg = "lightseagreen")
            #self.labelhelp2.place(x = 50, y = 560, width = 600, height = 30)

            self.canvas = tkinter.Canvas(self,width=912,height=203,scrollregion=(0,0,980,595))
            self.canvas.place(x = 100, y = 60) #放置canvas的位置

            self.mainFrame = tkinter.Frame(self.canvas)
            #self.mainFrame.config(padx='3.0m', pady='3.0m')
            self.mainFrame.place(width=200,height=190) #frame的长宽，和canvas差不多的


            self.vbar=tkinter.Scrollbar(self.canvas,orient=tkinter.VERTICAL) #竖直滚动条
            self.vbar.place(x = 898,width=20,height=207)
            self.vbar.configure(command=self.canvas.yview)

            self.canvas.config(yscrollcommand=self.vbar.set) #设置  
            self.canvas.create_window((456,298), window=self.mainFrame)  #create_window


            self.make_header()

            self.gridDict = {}
            for i in range(1, len(self.colList)):
                for j in range(len(self.rowList)):
                    w = EntryWidget(self.mainFrame, i, j+1)
                    self.gridDict[(i-1,j)] = w.value
                    def handler(event, col=i-1, row=j):
                        return self.__entryhandler(col, row)
                    w.bind(sequence="<FocusOut>", func=handler)


            self.buttonformcdmenuOverallPrimaryFilmStressok =tkinter.Button(self,text='应用',command=self.login, font = ("宋体",12),bg = 'silver')
            self.buttonformcdmenuOverallPrimaryFilmStressok.place(x = 130, y = 630, width = 60, height = 30)

            self.buttonformcdmenuOverallPrimaryFilmStresscancel = tkinter.Button(self,text='清除',command=self.cancel, font = ("宋体",12),bg = 'silver')
            self.buttonformcdmenuOverallPrimaryFilmStresscancel.place(x = 325, y = 630,width = 60,height = 30)

            self.buttonhelp = tkinter.Button(self,text='帮助',command=self.helpfile, font = ("宋体",12),bg = 'silver')
            self.buttonhelp.place(x = 520, y = 630,width = 60,height = 30)

            self.buttonlaststep = tkinter.Button(self,text='上一步',command=self.laststep, font = ("宋体",12),bg = 'silver')
            self.buttonlaststep.place(x = 715, y = 630,width = 60,height = 30)

            self.buttonnextstep = tkinter.Button(self,text='下一步',command=self.nextstep, font = ("宋体",12),bg = 'silver')
            self.buttonnextstep.place(x = 910, y = 630,width = 60,height = 30)

            self.textResult1 = tkinter.Text(self,width = 17, height = 2, font = ("宋体",12))
            self.textResult1.place(x = 120, y = 340)

            self.textResult = tkinter.Text(self,width = 17, height = 2, font = ("宋体",12))
            self.textResult.place(x = 420, y = 340)
            # self.textResult.focus()
            self.mainloop()

        def laststep(self):
            self.destroy()
            supportingT1330strainlimitframe1c()

        def nextstep(self):
            self.destroy()
            supportingunelasticB3c()


        def login(self):
            self.textResult.config(state = 'normal')
            self.textResult1.config(state = 'normal')
            self.textResult.delete('1.0','end')
            self.textResult1.delete('1.0','end')
            # self.textResult.focus()
            #'PL', 'Pb', 'QR', 'P', 'Q', 'F', 'E','Sm', 'σ1', 'σ2', 'σ3','n
            
            PL2 = self.PL
            Pb2 = self.Pb
            QR2 = self.QR
            P2 = self.P
            Q2 = self.Q
            F2 = self.F
            E2 = self.E
            Sm2 = self.Sm
            σ12 = self.σ1
            σ22 = self.σ2
            σ32 =self.σ3
            n2 = self.n

            

            if self.combobox.get() == "":
                tk.messagebox.showwarning("提示：","请选择材料的类型")
            else:
                cailiao = self.cailiao
            

            # Br1 = self.entryUsefactor.get()

            if PL2 == [] or Pb2 == [] or QR2 == [] or P2 == [] or Q2 == []  or F2 == [] or E2 ==[] or σ12 ==[] or σ22 ==[] or σ32 ==[] or Sm2 ==[] or n2 ==[]:#or cailiao ==''
                tkinter.messagebox.showwarning("警告","请完整输入")
            
            elif PL2 != [] or Pb2 != [] or QR2 != [] or P2 != [] or Q2 != []  or F2 != [] or E2 != [] or σ12 != [] or σ22 != [] or σ32 != [] or Sm2 != [] or n2!= []:#and cailiao !=''
                print("AAAAAAAA")
                print(PL2)
                print(Pb2)
                print(QR2)
                print(P2)
                print(Q2)
                print(F2)
                print(E2)
                print(Sm2)
                print(σ12)
                print(σ22)
                print(σ32)
                print(n2)
                #print(cailiao)
                print("BBBBb")

                print(len(PL2))
                for i in range(len(PL2)):
                    PL1 = PL2[i]
                    Pb1 = Pb2[i]
                    QR1 = QR2[i]
                    P1 = P2[i]
                    Q1 = Q2[i]
                    F1 = F2[i]
                    E1 = E2[i]
                    Sm1 = Sm2[i]
                    σ11 = σ12[i]
                    σ21 = σ22[i]
                    σ31 = σ32[i]
                    n1 = n2[i]

                    #输入值存入列表，只将PL放此处，为了判断PL列表长度是否与增量列表长度相同
                    #继而，完成出现应力不在工作区间直接报错。校核失败。
                    #unelasticB2aPL.append(PL1)

                    #global unelasticB2ayingbian
                    #print(unelasticB2ayingbian)
                    #根据薄膜应力等，计算出 X Y 值。接着运行xyz()函数，执行的是B-1图根据对应的区域选择对应的
                    #z值计算公式。应力等于z*SyL。B-1试验需要验证，应力是否在热端屈服应力范围内。验证成功后运用
                    #1.25倍的应力计算棘轮应变。

                    # 1 计算最大等效应变范围：  ('%.7g' % 1111.1111)
                    Δεmax= float('%.3g' % ((PL1+Pb1+QR1)/E1))
                    print(Δεmax)

                    # 2 计算修正的最大等效应变范围：
                    K = float('%.3g' % ((P1+Q1+F1)/(P1+Q1)))
                    print(K)

                    if K*Δεmax <= Sm1/E1:      #Sm1即为3Sm拔
                        Ke = 1
                    else:
                        Ke = K*Δεmax*E1/Sm1
                    
                    Δεmod = float('%.3g' % (Ke*K*Δεmax))
                    print(Δεmod)

                    # 3 计算多轴塑性和泊松比调整系数Kv：
                        # f由三向系数T.F确定
                    if σ11 + σ21 +σ31 >0:
                        abd = σ11 + σ21 +σ31
                    else:
                        abd = -(σ11 + σ21 +σ31)
                    TF = float('%.3g' % (abd/((1/math.sqrt(2))*math.sqrt((σ11 - σ21)*(σ11 - σ21) + (σ11 - σ31)*(σ11 - σ31) + (σ21 - σ31)*(σ21 - σ31)))))

                    print(TF)

                    name2=['x','y']
                    df = pd.read_excel('应力三轴度相关调整.xlsx', usecols='A:B', names=name2 ,index_col=None)

                    #采用numpy读取excel的数据并存入数组
                    x1 = np.array([x for x in df['x'].values if str(x) != 'nan'])
                    y1 = np.array([x for x in df['y'].values if str(x) != 'nan'])

                    TF = 1.06
                    fyingli3zhou = interpolate.interp1d(x1,y1,kind='cubic')
                    f = fyingli3zhou(TF)
                    print(f)


                    #f = 0.26
                    name2=['100x','100y']
                    df = pd.read_excel('塑性变形相关的泊松比调整.xlsx', usecols='A:B', names=name2 ,index_col=None)
                    x1 = np.array([x for x in df['100x'].values if str(x) != 'nan'])
                    y1 = np.array([x for x in df['100y'].values if str(x) != 'nan'])
                    fposongbi = interpolate.interp1d(x1,y1,kind='cubic')

                    PKv1 = float('%.2g' % (Ke*K*Δεmax*E1/Sm1))
                    if PKv1<1:
                        Kv1 = 1
                    elif PKv1 > 5:
                        Kv1 = 1.55
                    else:
                        PKv1 = float('%.2g' % (fposongbi(PKv1)))     #Δεmod = float('%.3g' % (Ke*K*Δεmax))
                    print(PKv1)
                    #Kv1 = 1
                    Kv = 1 + f*(Kv1 - 1)

                    # 4 计算总应变范围εc:  
                    #此处1.25为Kt 看横截面的截面系数确定
                    Sy = 170
                    Z1 = (PL1+(Pb1/1.25))/Sy
                    
                    σc =Z1  * Sy
                        #εc太小忽略:
                    Δεc = 0

                    # 5 计算总应变范围εt:
                    εt = float('%.3g' % (Kv * Δεmod + K *Δεc))

                    print(εt)
                    print(n1)
                    #读取通过getdata获取的数据点文件
                    #可通过两种方式绝对地址和相对地址
                    #file_path = r'D:\sss\python\1420-1.xlsx'
                    name2=['x','y']
                    df = pd.read_excel('1420-1.xlsx', usecols='A:B', names=name2 ,index_col=None)

                    #采用numpy读取excel的数据并存入数组
                    x1 = np.array([x for x in df['x'].values if str(x) != 'nan'])
                    y1 = np.array([x for x in df['y'].values if str(x) != 'nan'])

                    t2 = εt
                    if t2>0.1 or t2 <0.0001:
                        tk.messagebox.showwarning("提示：","数据超出范围")
                    elif 0.0001<t2:
                        z = 1000000
                    elif t2 < 0.05:
                        z = 10
                    else:
                        f = interpolate.interp1d(y1,x1,kind='cubic')
                        z=f(t2)
                    print('mmmmmm')
                    print(t2)
                    print(z)

                    # else:
                    #     #弹窗：载荷应力大于热端屈服应力，试验B-1不适用。
                    #     tk.messagebox.showwarning("警告", "载荷应力大于热端屈服应力，试验B-1不适用。")
                print("**####*****")
                unelasticB2ayingbian = 10
                result3 = n1/z
                self.textResult.insert('insert',"%.8f"%unelasticB2ayingbian)
                self.textResult1.insert('insert',result3)
                self.textResult.config(state = 'disabled')
                self.textResult1.config(state = 'disabled')
                global unelasticB2aresult
                unelasticB2aresult = result3

                #x=np.linspace(0,10,11)
                x=[0,0.3,1]
                y=[1,0.3,0]
                #y=np.sin(x)
                x1=np.linspace(0,1,101)
                f = interpolate.interp1d(x,y,kind = 'slinear')
                y1 = f(x1) 


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
                sonFrame = tk.Frame(self, sonFrameSetting)
                sonFrame.place(x=670,y=290)

                fig = Figure(figsize=(5,4), dpi=80)
                ax1 = fig.add_subplot(111)

                ax1.set(xlim=[0,1],ylim=[0,1],)

            #ax1.set_xscale('log')
            #ax1.set_yscale('log',)
    # ax1.set_yscale('log',basey =2)
                ax1.set_title('蠕变-疲劳损伤包络线(316/304)',fontsize=12)
            #ax1.set_xlabel('11',fontsize=12)
            #ax1.set_ylabel('22',fontsize=12)
    # ax1.set_xticks([10,10**2,10**3,10**4,10**5,3*10**5,],)
    # ax1.set_yticks([6.9,14,34,69,140,340,690],)
                ax1.tick_params(labelsize=10) #刻度字体大小13
                ax1.grid(True,which="both",ls="-") 
                
    #ax1.plot(x1,y1,color = 'blue')#line1, = 
                #leg1 = ax1.legend(handles=[line1], fontsize=9,loc=[0.8,0.7],frameon=False,handlelength=0)
                #ax1.add_artist(leg1)
                ax1.plot(x1,y1,color = 'black', label = "427",)
    #line2, = ax1.plot(x2,y2,color = 'blue', label = "454",)
    #line3, = ax1.plot(x3,y3,color = 'cadetblue', label = "482",)
    #line4, = ax1.plot(x4,y4,color = 'gray', label = "510",)
    #line5, = ax1.plot(x5,y5,color = 'darkcyan', label = "538",)
                #ax1.text(40000,525,'Temperature,℃',size =10)

                z = 0.5
                t2 = 0.3

                ax1.text(0.25,0.75,'计算值坐标：',size =10, color = 'red',)
                ax1.scatter(z,t2,color = 'red',)
                ax1.text(0.5,0.75,'(%.3f, %.3f)' %(z, t2),color ='r',size =10)

                # 将绘制的图形显示到tkinter:创建属于root的canvas画布,并将图f置于画布上
                canvas = FigureCanvasTkAgg(fig, master=sonFrame)
    # 注意show方法已经过时了,这里改用draw
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, ) # 上对齐





        def cancel(self):
            self.textResult.config(state = 'normal')
            self.textResult1.config(state = 'normal')
            self.textResult.delete('1.0','end')
            self.textResult1.delete('1.0','end')
            # self.varUsefactor.set('')
            self.demo()
            #'PL', 'Pb', 'QR', '一次', '二次', '峰值', 'E','3Sm', 'σ1', 'σ2', 'σ3'
            del self.PL[:]
            del self.Pb[:]
            del self.QR[:]
            del self.P[:]
            del self.Q[:]
            del self.F[:]
            del self.E[:]
            del self.Sm[:]
            del self.σ1[:]
            del self.σ2[:]
            del self.σ3[:]
            del self.n[:]
            self.combobox.set("")
            # del self.Td[:]
            
        def helpfile(self):
            import tkinter as tk
            helpwindow = tk.Toplevel()
            helpwindow.title('帮助')
            helpwindow.geometry('800x660+400+100')

            helplabel1 = tk.Label(helpwindow, 
                        text = '设计步骤：', 
                        fg = "red",

                        font = ("宋体",14),
                    justify = 'left',anchor= 'nw')
            
            helplabel1.place(x= 20,y =15, width = 610, height = 440)


            helplabel2 = tk.Label(helpwindow, 
                        text = '''
    弹性模量E查找 ASME II-D。

                     X =(PL+Pb/Kt)÷Sy             Y =(QR)/Sy  

    其中：（PL+Pb/Kt）为循环中对弯曲应力按Kt调整的一次应力强度的最大值；
    
    Sy为评定的循环中最高和最低沿壁厚平均温度下Sy的值的平均值。
    
    QR 为所考虑循环中的二次应力强度的最大范围。
    
    带入计算的X、Y带入试验B-2的简化非弹性分析的有效蠕变应力参数Z图，计算出无量纲无量

    纲有效蠕变应力参数Z，从而确定此步条件下的蠕变应变，接着根据温度、时间、计算的1.25
    
    倍的蠕变应力选择对应的等时应力应变曲线图，根据工作时间，蠕变应力得到此步的应变值，
    
    全部的使用寿期可以划分成多个温度时间段。


    各段的蠕变应力各不相同，但在每段的使用时间内蠕变应力始终保持不变。在计算棘轮应变

    时，需考虑初始应变的影响，上一步的应变在下一步计算时，为初始应变。即对每段，等时

    曲线可在前面整个载荷历程所累积的初始应变上形成。 每个时间-温度时间段的蠕变应变增
    
    量应相加，以得到总的棘轮蠕变应变，结果对母材应限制在1%，对焊缝金属应限制在0.5%。





        
        
        ''', 

                        font = ("宋体",13), 
                justify = 'left',fg = 'lightseagreen',anchor= 'nw')
            
            helplabel2.place(x= 28,y =35, width = 780, height = 840)


            helplabel3 = tk.Label(helpwindow, 
                        text = '提醒:', 
                        fg = "red",

                        font = ("宋体",14),
                    justify = 'left',anchor= 'nw')
            
            helplabel3.place(x= 20,y =520, width = 720, height = 440)



            helplabel4 = tk.Label(helpwindow, 
                        text = '''
    一定要注意所填写数据的单位是否匹配。不可输入非数字，以免影响计算结果。
        ''', 

                        font = ("宋体",13),
                    justify = 'left',anchor= 'nw')
            
            helplabel4.place(x= 28,y =550, width = 720, height = 440)


            helpwindow.mainloop()

     
        def make_header(self):
            self.hdrDict = {}
            self.PL = []
            self.Pb = []
            self.QR = []
            self.P = []
            self.Q = []
            self.F = []
            self.E = []
            self.Sm = []
            self.σ1 = []
            self.σ2 = []
            self.σ3 = []
            self.n = []
            # self.Td = []
            for i, label in enumerate(self.colList):
                def handler(event, col=i, row=0, text=label):
                    return self.__entryhandler(col, row, text)
                w = LabelWidget(self.mainFrame, i, 0, label)
                self.hdrDict[(i,0)] = w
                w.bind(sequence="<KeyRelease>", func=handler)

            for i, label in enumerate(self.rowList):
                def handler(event, col=0, row=i+1, text=label):
                    return self.__entryhandler(col, row, text)
                w = LabelWidget(self.mainFrame, 0, i+1, label)
                self.hdrDict[(0,i+1)] = w
                w.bind(sequence="<KeyRelease>", func=handler)

        def __entryhandler(self, col, row):
            s = self.gridDict[(col,row)].get()
            # if s.upper().strip() == "EXIT":
            #     self.destroy()
            # elif s.upper().strip() == "DEMO":
            #     self.demo()
            if s != "":
                s = float(s.strip())
                #print(s)
                #print(row)
                #'PL', 'Pb', 'QR', 'P', 'Q', 'F', 'E','Sm', 'σ1', 'σ2', 'σ3'

                if col == 0:
                    if row == len(self.PL):
                        self.PL.append(s)
                    elif row < len(self.PL):
                        self.PL[row]= s     
                    # print(s)

                if col == 1:
                    if row == len(self.Pb):
                        self.Pb.append(s)
                    elif row < len(self.Pb):
                        self.Pb[row]= s 
                    # print(s)
                
                if col == 2:
                    if row == len(self.QR):
                        self.QR.append(s)
                    elif row < len(self.QR):
                        self.QR[row]= s

                if col == 3:
                    if row == len(self.P):
                        self.P.append(s)
                    elif row < len(self.P):
                        self.P[row]= s
                #'PL', 'Pb', 'Kt', 'SyL', 'QR', 'SyH', 'time', 'T'

                if col == 4:
                    if row == len(self.Q):
                        self.Q.append(s)
                    elif row < len(self.Q):
                        self.Q[row]= s

                if col == 5:
                    if row == len(self.F):
                        self.F.append(s)
                    elif row < len(self.F):
                        self.F[row]= s

                if col == 6:
                    if row == len(self.E):
                        self.E.append(s)
                    elif row < len(self.E):
                        self.E[row]= s

                if col == 7:
                    if row == len(self.Sm):
                        self.Sm.append(s)
                    elif row < len(self.Sm):
                        self.Sm[row]= s

                if col == 8:
                    if row == len(self.σ1):
                        self.σ1.append(s)
                    elif row < len(self.σ1):
                        self.σ1[row]= s

                if col == 9:
                    if row == len(self.σ2):
                        self.σ2.append(s)
                    elif row < len(self.σ2):
                        self.σ2[row]= s

                if col == 10:
                    if row == len(self.σ3):
                        self.σ3.append(s)
                    elif row < len(self.σ3):
                        self.σ3[row]= s

                if col == 11:
                    if row == len(self.n):
                        self.n.append(s)
                    elif row < len(self.n):
                        self.n[row]= s
                # if col == 3:
                #     if row == len(self.Td):
                #         self.Td.append(s)
                #     elif row < len(self.Td):
                #         self.Td[row]= s
            
                
                # print(self.n)
                # print(self.Nd)
                # print(self.Δt)
                # print(self.Td)

        def demo(self):
            ''' enter a number into each Entry field '''
            for i in range(len(self.cols)):
                for j in range(len(self.rowList)):
                    # sleep(0.25)
                    self.set(i,j,"")
        #             self.update_idletasks()
        #             sleep(0.1)
        #             self.set(i,j,i+1+j)
        #             self.update_idletasks()

        def __headerhandler(self, col, row, text):
            ''' has no effect when Entry state=readonly '''
            self.hdrDict[(col,row)].text.set(text)

        def get(self, x, y):
            return self.gridDict[(x,y)].get()

        def set(self, x, y, v):
            self.gridDict[(x,y)].set(v)
            return v

    if __name__ == "__main__":
        cols = ['PL', 'Pb', 'QR', 'P', 'Q', 'F', 'E','Sm', 'σ1', 'σ2', 'σ3','n']
        rows = ['1', '2', '3', '4','5', '6', '7', '8', '9', '10', 
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
        '21','22', '23', '24', '25',]
        app = EntryGrid(cols, rows)

#B-2号试验
supportingunelasticB2c()