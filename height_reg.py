import numpy as np
import matplotlib.pyplot as plt

np.random.seed(seed=1)

lo=4
hi=30
n=10
x=5+25*np.random.rand(n)

c=[170,108,0.2]
t=c[0]-c[1]*np.exp(-c[2]*x)\
    +4*np.random.randn(n)
print(np.round(x,3))
print(np.round(t,3))
np.savez("height_reg.npz",X=x,X_min=lo,X_max=hi,X_n=n,T=t)

plt.figure(figsize=(4,4))
plt.plot(x,t,marker="o",linestyle="None",markeredgecolor="black",
color="cornflowerblue")

plt.xlim(lo,hi)
plt.grid(True)

plt.show()