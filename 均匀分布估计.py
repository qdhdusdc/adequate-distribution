import matplotlib.pyplot as plt
import numpy as np
from random import sample
fig=plt.figure()
a,b=5,10   #X~U(a,b)
#n=50000      #随机数个数
m=20       #随机抽取样本
aM,bM,aL,bL,EA,EB,std_a,std_b=[],[],[],[],[],[],[],[]
for i in range(0,1000000):
    sample=a+(b-a)*np.random.random(m)
    
    # X=X.tolist()
    # sample=sample(X,m)
    # sample=np.array(sample)
    EX=(a+b)/2
    DX=(b-a)**2/12
    
    M1=np.mean(sample)         #一阶样本距
    M2=(sum((sample-M1)**2))/m      #二阶样本距
    S_2=m*M2/(m-1)    #样本方差
    a_M=M1-np.sqrt(3*M2)  #矩估计a
    b_M=M1+np.sqrt(3*M2)  #矩估计b
    a_L=min(sample)
    b_L=max(sample)
    Ea=M1-np.sqrt(3*S_2)  #无偏估计a
    Eb=M1+np.sqrt(3*S_2)  #无偏估计b
    stda=(m*a_L-b_L)/(m-1)
    stdb=(m*b_L-a_L)/(m-1)
    aM.append(a_M)
    bM.append(b_M)    
    aL.append(a_L)
    bL.append(b_L)
    EA.append(Ea)
    EB.append(Eb)    
    std_a.append(stda)
    std_b.append(stdb)
# plt.hist(X, 50,label='均匀分布',alpha=0.75,density=True)
# plt.axhline(y=0.2,ls="-",c="red")
# plt.rcParams.update({'font.size': 18})
# plt.ylabel("P")
# plt.xlabel("X")

# print("EX:"+"%s"%EX)
# print("DX:"+"%s"%DX)
# print("M1:"+"%s"%M1)
# print("M2:"+"%s"%M2)
# print("S_2:"+"%s"%S_2)
# print("S_2:"+"%s"%S_2)
print("样本数:"+"%s"%m)
print("矩估计a:"+"%s"%np.mean(aM)+"矩估计b:"+"%s"%np.mean(bM))
print("极大似然估计a:"+"%s"%np.mean(aL)+"极大似然估计b:"+"%s"%np.mean(bL))
print("样本方差估计a:"+"%s"%np.mean(EA)+"样本方差估计b:"+"%s"%np.mean(EB))
print("无偏估计a:"+"%s"%np.mean(std_a)+"无偏估计b:"+"%s"%np.mean(std_b))

