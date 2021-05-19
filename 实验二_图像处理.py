# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt #加载matplotlib库作为plt
import numpy as np  #加载numpy库作为np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100) #x范围从0到3π，间隔为100
y = np.sin(x) #y为sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1) #图像为一行第一列
plt.title(r'$f(x)=sin(x)$') #图像标题
plt.plot(x, y) #绘制x轴，y轴
#plt.show()

x1 = [t*0.375*np.pi for t in x] #x1范围为x的范围，间隔为0.375π，
y1 = np.sin(x1) #y1为sin(x1)
plt.subplot(1,2,2) #图像为一行第二列
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #图像标题
plt.plot(x1, y1) #绘制x1，y1轴
plt.show() #显示两个图像