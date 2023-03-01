#温兆和 10205501432 数学基础作业6 5（2）
import os  # 修改工作目录
import numpy as np
from numpy.linalg import solve
import pandas as pd
import scipy.stats as stats  # 统计函数
import matplotlib.pyplot as plt
from plotnine import *  # ggplot 绘图
from plotnine.data import mpg
from jupyterquiz import display_quiz  # Quiz
import random
import math
def max(v):
    ans = v[0]
    for i in range(len(v)):
        if v[i]>ans:
            ans = v[i]
    return ans
#输入矩阵、初始向量、误差极限和最大迭代次数
A = np.array([[5,-1,1],[-1,2,0],[1,0,3]])
N = 1000000
v=np.array([1,1,1])
epsilon = 0.001
#定义幂法函数
def MiFa(A,v,N,epsilon):
    m=max(v)
    for i in range(N):
        v_apostrophe = A@v
        m_apostrophe = max(v_apostrophe)
        v_apostrophe = v_apostrophe / m_apostrophe
        if math.fabs(m-m_apostrophe)<epsilon:
            return m_apostrophe
            break
        m = m_apostrophe
        v = v_apostrophe
    #如果超过迭代次数仍未收敛就报错
    return -1000000
#定义反幂法函数
def FanMiFa(A,v,N,epsilon):
    m=max(v)
    v=v/m
    for i in range(N):
        x = solve(A,v)
        m_apostrophe = max(x)
        x=x/m_apostrophe
        if math.fabs(1/m-1/m_apostrophe)<epsilon:
            return m_apostrophe
            break
        m = m_apostrophe
        v = x
    #如果超过迭代次数仍未收敛就报错
    return -1000000
#用幂法求解主特征值
lamda_1 = MiFa(A,v,N,epsilon)
#用反幂法求解最小特征值的倒数
lamda_3 = FanMiFa(A,v,N,epsilon)
print('The condition number is:')
print(math.fabs(lamda_1*lamda_3))
#检查结果是否正确
eigenvalue_max,featurevector_max=np.linalg.eig(A)
A_ni = np.linalg.inv(A)
eigenvalue_min,featurevector_min=np.linalg.eig(A_ni)
print('The correct answer is:')
print(math.fabs(max(eigenvalue_max)*max(eigenvalue_min)))
#运算结果为：
#The condition number is:
#3.474347567396835
#The correct answer is:
#3.482316580832219
#我们用幂法算出来的条件数和我们调用Python包算出来的条件数差不多，说明这段代码是正确的。