import numpy as np
import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # Solve the minus sign problems
plt.figure( dpi=1000)
x=[2,3,4,5,10,20,40,60]
y1=[5]*len(x)
y2=[10]*len(x)

y5=[6.07,5.64,5.45,5.34,5.16,5.08,5.04,5.0245,]#矩估计a
y6=[8.95,9.37,9.55,9.65,9.84,9.92,9.96,9.9743,]#矩估计b
y3=[6.67,6.25,6.00,5.83,5.46,5.24,5.12,5.0815,]#极大似然估计a
y4=[8.34,8.76,9.00,9.16,9.55,9.76,9.88,9.9182,]#极大似然估计b
y7=[5.47,5.22,5.13,5.09,5.04,5.0133,5.0078,5.0037,]#无偏估计a
y8=[9.54,9.79,9.87,9.90,9.96,9.9871,9.9952,9.9951]#无偏估计b
y9=[5.004,5.000,5.001,5.001,5.001,5.000,5.000,5.000]
y10=[10.002,9.997,9.995,10.000,10.002,10.001,10.000,10.000]

plt.plot(x,y1,c='black',label='a')
plt.plot(x,y2,c='black',label='b')
plt.plot(x,y3,c='orange', label='极大似然估计a',linestyle = '--')
plt.plot(x,y4,c='orange',label='极大似然估计b',linestyle='-.')
plt.plot(x,y5,c='green',label='矩估计估计a', linestyle = '--')
plt.plot(x,y6,c='green',label='矩估计估计b' ,linestyle = '-.')
plt.plot(x,y7,c='purple',label='样本方差估计a', linestyle = '--')
plt.plot(x,y8,c='purple',label='样本方差估计b', linestyle = '-.')
plt.plot(x,y9,c='red',label='无偏估计a',alpha=0.5, linestyle = '--')
plt.plot(x,y10,c='red',label='无偏估计b', alpha=0.5,linestyle = '-.')
plt.legend(loc='upper right')
plt.legend(ncol=2)
plt.rc('font', size=10)

plt.title("均匀分布的估计",fontsize=15)
plt.xlabel("样本数",fontsize=13)
plt.ylabel("估计值",fontsize=13)
plt.show()

