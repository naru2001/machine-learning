import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


def gauss(x, mu, sigma):
    N, D = x.shape
    c1 = 1/(2*np.pi)**(D/2)
    c2 = 1/(np.linalg.det(sigma)**0.5)

    inv_sigma = np.linalg.inv(sigma)
    c3 = x-mu
    c4 = np.dot(c3, inv_sigma)
    c5 = np.zeros(N)

    for d in range(D):
        c5 += c4[:, d]*c3[:, d]
    p = c1*c2*np.exp(-c5/2)
    return p


x = np.array([[1, 2], [2, 1], [3, 4]])
mu = np.array([1, 2])
sigma = np.array([[1, 0], [0, 1]])
print(gauss(x, mu, sigma))

xr0 = [-3, 3]
xr1 = [-3, 3]


def scg(mu, sig):
    xn = 40
    x0 = np.linspace(xr0[0], xr0[1], xn)
    x1 = np.linspace(xr1[0], xr1[1], xn)
    xx0, xx1 = np.meshgrid(x0, x1)
    x = np.c_[np.reshape(xx0, xn * xn, order="F"), np.reshape(xx1, xn * xn, order="F")]
    f = gauss(x, mu, sig)
    f = f.reshape(xn, xn)
    f = f.T
    cont = plt.contour(xx0, xx1, f, 15, colors='k')
    plt.grid(True)


def show3d(ax, mu, sig):
    xn = 40
    x0 = np.linspace(xr0[0], xr0[1], xn)
    x1 = np.linspace(xr1[0], xr1[1], xn)
    xx0, xx1 = np.meshgrid(x0, x1)
    x = np.c_[np.reshape(xx0, xn*xn, order="F"), np.reshape(xx1, xn*xn, order="F")]
    f = gauss(x, mu, sig)
    f = f.reshape(xn, xn)
    f = f.T
    ax.plot_surface(xx0, xx1, f, rstride=2, cstride=2,
                    alpha=0.3, color="blue", edgecolor="black")


mu = np.array([1, 0.5])
sigma = np.array([[2, 1], [1, 1]])
fig = plt.figure(1, figsize=(7, 3))
fig.add_subplot(1, 2, 1)
scg(mu, sigma)
plt.xlim(xr0)
plt.ylim(xr1)
plt.xlabel("$x_0$", fintsize=14)
plt.xlabel("$x_1$", fintsize=14)
ax = fig.add_subplot(1, 2, 2, projection="3d")
show3d(ax, mu, sigma)
ax.set_zticks([0.05, 0.10])
ax.set_xlabel("$x_0$", fontsize=14)
ax.set_ylabel("$x_1$", fontsize=14)
ax.view_init(40, -100)

plt.show()
