import numpy as np
import matplotlib.pyplot as plt


def f(w0, w1):
    return w0**2+2*w0*w1+3


def df_dw0(w0, w1):
    return 2*w0+2*w1


def df_dw1(w0, w1):
    return 2*w0+0*w1


w_range = 2
dw = 0.25
w0 = np.arange(-w_range, w_range+dw, dw)
w1 = np.arange(-w_range, w_range+dw, dw)

ww0, ww1 = np.meshgrid(w0, w1)
ff = np.zeros((len(w0), len(w1)))

dff_dw0 = np.zeros((len(w0), len(w1)))
dff_dw1 = np.zeros((len(w0), len(w1)))
for i in range(len(w0)):
    for j in range(len(w1)):
        ff[j, i] = f(w0[i], w1[j])
        dff_dw0[j, i] = df_dw0(w0[i], w1[j])
        dff_dw1[j, i] = df_dw1(w0[i], w1[j])

plt.figure(figsize=(9, 4))
plt.subplots_adjust(wspace=0.3)
plt.subplot(1, 2, 1)
cont = plt.contour(ww0, ww1, ff, 10, colors="k")
cont.clabel(fmt="%d", fontsize=8)
plt.xticks(range(-w_range, w_range+1, 1))
plt.yticks(range(-w_range, w_range+1, 1))
plt.xlim(-w_range-0.5, w_range+0.5)
plt.ylim(-w_range-0.5, w_range+0.5)
plt.xlabel('$w_0$', fontsize=14)
plt.ylabel('$w_1$', fontsize=14)

plt.subplot(1, 2, 2)
plt.quiver(ww0, ww1, dff_dw0, dff_dw1)
plt.xlabel("$w_0$", fontsize=14)
plt.ylabel("$w_1$", fontsize=14)
plt.xticks(range(-w_range, w_range+1, 1))
plt.yticks(range(-w_range, w_range+1, 1))
plt.xlim(-w_range-0.5, w_range+0.5)
plt.ylim(-w_range-0.5, w_range+0.5)
plt.show()
