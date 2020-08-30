import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

def f(a):
    u=sum(np.exp(i) for i in a)
    return [np.exp(i)/u for i in a]

xn=20

x0=np.linspace(-4,4,xn)
x1=np.linspace(-4,4,xn)

y=np.zeros((xn,xn,3))

for i in range(xn):
    for j in range(xn):
        y[j,i,:]=f([x0[i],x1[j],1])

xx0,xx1=np.meshgrid(x0,x1)
plt.figure(figsize=(8,3))

for i in range(2):
    ax=plt.subplot(1,2,i+1,projection="3d")
    ax.plot_surface(xx0,xx1,y[:,:,i],rstride=1,cstride=1,alpha=0.3,
                    color="blue",edgecolor="black")
    ax.set_xlabel("$x_0$",fontsize=14)
    ax.set_ylabel("$x_1$",fontsize=14)
    ax.view_init(40,-125)

plt.show()