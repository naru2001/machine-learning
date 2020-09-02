from matplotlib.pyplot import figimage
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mse_line(x,t,w):
    y=w[0]*x+w[1]
    mse=np.mean((y-t)**2)
    return mse

np.random.seed(seed=1)
n=10
x=5+25*np.random.rand(n)

c=[170,108,0.2]
t=c[0]-c[1]*np.exp(-c[2]*x)+4*np.random.randn(n)

xn=100
wr0=[-25,25]
wr1=[120,170]
w0=np.linspace(wr0[0],wr0[1],xn)
w1=np.linspace(wr1[0],wr1[1],xn)

ww0,ww1=np.meshgrid(w0,w1)
j=np.zeros((len(w0),len(w1)))

for i in range(len(w0)):
    for k in range(len(w1)):
        j[k,i]=mse_line(x,t,(w0[i],w1[k]))

plt.figure(figsize=(9.5,4))
plt.subplots_adjust(wspace=0.5)

ax=plt.subplot(1,2,1,projection="3d")
ax.plot_surface(ww0,ww1,j,rstride=10,cstride=10,alpha=0.3,
color="blue",edgecolor="black")
ax.set_xticks([-20,0,20])
ax.set_yticks([120,140,160])
ax.view_init(20,-60)

plt.subplot(1,2,2)
cont=plt.contour(ww0,ww1,j,30,colors="black",levels=[100,1000,10000,100000])
cont.clabel(fmt="%d",fontsize=8)
plt.grid(True)

plt.show()