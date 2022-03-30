import tkinter as tk
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import easygui
flag = False
lists = []
trainlist = []
count = 0
trainnumber = 0
testnumber = 0
tempcount = 0
degree = 0
colordot = ['cyan','gray','green','hotpink','blue',
'chocolate','gold']
window = tk.Tk()
var1 = tk.DoubleVar()
var2 = tk.DoubleVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
# var4 = tk.DoubleVar()
# var5 = tk.DoubleVar()
# var6 = tk.DoubleVar()
var3.set("尚未選擇檔案")
# 設定視窗標題、大小和背景顏色
window.title('感知機')
window.geometry('600x400')
window.configure(background='white')


l1 = tk.Label(window, text = "請輸入學習率",font=('Arial', 10),bg = "gray", width = 12, height = 2 )
l1.place(x=10,y=20)
l2 = tk.Label(window, text = "請輸入學習次數",font=('Arial', 10),bg = "gray", width = 12, height = 2 )
l2.place(x=10,y=80)
l3 = tk.Label(window, text = "訓練正確率",font=('Arial', 10),bg = "gray", width = 12, height = 2 )
l3.place(x=10,y=210)
l4 = tk.Label(window, text = "測試正確率",font=('Arial', 10),bg = "gray", width = 12, height = 2 )
l4.place(x=10,y=250)
l5 = tk.Label(window, textvariable=var1,font=('Arial', 10),bg = "yellow", width = 12, height = 2 )
l5.place(x=130,y=210)
l6 = tk.Label(window, textvariable=var2,font=('Arial', 10),bg = "yellow", width = 12, height = 2 )
l6.place(x=130,y=250)
l7 = tk.Label(window, textvariable=var3,font=('Arial', 10),fg = "red",bg = "white",  height = 2 )
l7.place(x=150,y=130)
l8 = tk.Label(window, text = "最後鍵結值",font=('Arial', 10),bg = "gray", width = 12, height = 2 )
l8.place(x=10,y=290)
l9 = tk.Label(window, textvariable=var4,font=('Arial', 10),bg = "yellow", height = 2 )
l9.place(x=130,y=290)
# l9 = tk.Label(window, textvariable=var4,font=('Arial', 10),bg = "yellow", width = 12, height = 2 )
# l9.place(x=130,y=290)
# l10 = tk.Label(window, textvariable=var5,font=('Arial', 10),bg = "yellow", width = 12, height = 2 )
# l10.place(x=250,y=290)
# l11 = tk.Label(window, textvariable=var6,font=('Arial', 10),bg = "yellow", width = 12, height = 2 )
# l11.place(x=370,y=290)

e1 = tk.Entry(window, show=None,width = 10)   
e2 = tk.Entry(window, show=None,width = 10)  # 顯示成明文形式

e1.place(x=130,y=30)
e2.place(x=130,y=90)

var = tk.StringVar()
def select_file():

    path = easygui.fileopenbox()
    file = open(path, mode="r")
    var3.set(path)
    global lists,trainlist,count,trainnumber,testnumber,tempcount,flag,degree,colordot
    flag = True
    lists = []
    trainlist = []
    for line in file:
        list = line.split()
        lists.append(list)
    degree = len(lists[0]) - 1
    count = len(lists)
    trainnumber = math.ceil(count * 2 / 3)
    testnumber = count - trainnumber
    tempcount = count-1
    for i in range(0,trainnumber):
        r = random.randint(0,tempcount)
        tempcount -= 1
        trainlist.append(lists[r])
        lists[r:r+1] = []
    
def gogo():
    global lists,trainlist,count,trainnumber,testnumber,tempcount,var1,var2,degree
    weight = []
    for i in range(degree+1):
        weight+=[random.uniform(-1,1)]
    learnrate = float(e1.get())
    times = int(e2.get())
    ans = []
    for i in range(degree+1):
        ans+=[weight[i]]
    tcorrectrate = 0
    tcorrectnumber = 0
    sum = 0
    fcorrectnumber = 0
    while times>0:
        for i in range(0,trainnumber):
            sum = -1 * weight[0]
            for j in range(0,degree):
                sum += weight[j+1]*float(trainlist[i][j])
            if (sum <= 0 and float(trainlist[i][degree])%2 == 0 and float(trainlist[i][degree]) != 4):
                weight[0] += -1 * learnrate
                for k in range(0,degree):
                    weight[k+1] += learnrate * float(trainlist[i][k])
            elif (sum >= 0 and float(trainlist[i][degree])%2 == 1):
                weight[0] -= -1 * learnrate
                for k in range(0,degree):
                    weight[k+1] -= learnrate * float(trainlist[i][k])
            for j in range(0,trainnumber):
                sum = -1 * weight[0]
                for k in range(0,degree):
                    sum += weight[k+1]*float(trainlist[j][k])
                if(sum < 0 and float(trainlist[j][degree])%2 == 1):
                    tcorrectnumber += 1
                elif (sum > 0 and float(trainlist[j][degree])%2 == 0 and float(trainlist[i][degree]) != 4):
                    tcorrectnumber += 1
            if( tcorrectrate < tcorrectnumber / trainnumber):
                tcorrectrate = tcorrectnumber / trainnumber
                for  p in range(0,degree+1):
                    ans[p] = weight[p]
            tcorrectnumber = 0
            times -= 1
            if(times<=0):
                break
    plt.subplot(2, 1, 1)
    x = np.arange(-10,10,1)
    y = [i * -(ans[1]/ans[2]) + ans[0]/ans[2] for i in x]
    plt.plot(x, y)
    for i in range(0,trainnumber):
        if(float(trainlist[i][degree])%2 == 1):
            plt.scatter(float(trainlist[i][0]),float(trainlist[i][1]),s=5,color = colordot[int(trainlist[i][degree])])
        elif(float(trainlist[i][degree])%2 == 0 and float(trainlist[i][degree]) != 4):
            plt.scatter(float(trainlist[i][0]),float(trainlist[i][1]),s=5,color = colordot[int(trainlist[i][degree])])
        else:
            plt.scatter(float(trainlist[i][0]),float(trainlist[i][1]),s=5,color = colordot[int(trainlist[i][degree])])
    plt.title("training result")  
    #上方是訓練資料圖


    for j in range(0,count - trainnumber):
        sum = -1 * ans[0]
        for k in range(0,degree):
            sum += ans[k+1]*float(lists[j][k])
        if(sum < 0 and float(lists[j][degree])%2 == 1):
            fcorrectnumber += 1
        elif (sum > 0 and float(lists[j][degree])%2 == 0 and float(lists[j][degree]) != 4):
            fcorrectnumber += 1  
    #上方是測試資料

    plt.subplot(2, 1, 2)
    plt.plot(x,y)
    for i in range(0,count - trainnumber):
        if(float(lists[i][degree])%2 == 1):
            plt.scatter(float(lists[i][0]),float(lists[i][1]),s=5,color = colordot[int(lists[i][degree])])
        elif(float(lists[i][degree])%2 == 0 and float(trainlist[i][degree]) != 4):
            plt.scatter(float(lists[i][0]),float(lists[i][1]),s=5,color = colordot[int(lists[i][degree])])
        else:
            plt.scatter(float(lists[i][0]),float(lists[i][1]),s=5,color = colordot[int(lists[i][degree])])
    plt.title("testing result")
    var1.set(round(tcorrectrate,5))
    var2.set(round(fcorrectnumber/testnumber,5))
    w = ''
    for i in range(degree+1):
        w += str(round(ans[i],5))
        w+= ", "
    var4.set(w)
    # var4.set(round(ans[0],5))
    # var5.set(round(ans[1],5))
    # var6.set(round(ans[2],5))
    plt.show()
    #上方是測試資料圖




b1 = tk.Button(window, text='請選擇檔案', font=('Arial', 12), width=10, height=1,command=select_file)
b1.place(x=10,y=130)
b2 = tk.Button(window, text='開始訓練', font=('Arial', 12), width=10, height=1,command=gogo)
b2.place(x=80,y=170)



window.mainloop()