import numpy as np
import matplotlib.pyplot as plt

def mse_line(x,t,w):
    y=w[0]*x+w[1]
    mse=np.mean((y-t)**2)
    return mse

def dmse_line(x,t,w):
    y=w[0]*x+w[1]
    dw_0=2*np.mean((y-t)*x)
    dw_1=2*np.mean(y-t)
    return dw_0,dw_1

np.random.seed(seed=1)
n=16
x=5+25*np.random.rand(n)

c=[170,108,0.2]
t=c[0]-c[1]*np.exp(-c[2]*x)+4*np.random.randn(n)

xn=10
wr0=[-25,25]
wr1=[120,170]
w0=np.linspace(wr0[0],wr0[1],xn)
w1=np.linspace(wr1[0],wr1[1],xn)

ww0,ww1=np.meshgrid(w0,w1)
j=np.zeros((len(w0),len(w1)))

for i in range(len(w0)):
    for k in range(len(w1)):j[k,i]=mse_line(x,t,(w0[i],w1[k]))

d_w=dmse_line(x,t,[10,165])
print(np.round(d_w,1))