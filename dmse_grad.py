import numpy as np
import matplotlib.pyplot as plt


def fit_line_num(x, t):
    w_init = [10.0, 165.0]
    alpha = 0.001
    tau_max = 100000
    eps = 0.1
    w_hist = np.zeros([tau_max, 2])
    w_hist[0, :] = w_init
    dmse, tau = None, None
    for tau in range(1, tau_max):
        dmse = dmse_line(x, t, w_hist[tau-1])
        w_hist[tau, 0] = w_hist[tau-1, 0]-alpha*dmse[0]
        w_hist[tau, 1] = w_hist[tau-1, 1]-alpha*dmse[1]
        if max(np.absolute(dmse)) < eps:
            break

    w0 = w_hist[tau, 0]
    w1 = w_hist[tau, 1]
    w_hist = w_hist[:tau, :]
    return w0, w1, dmse, w_hist


def mse_line(x, t, w):
    y = w[0]*x+w[1]
    mse = np.mean((y-t)**2)
    return mse


def dmse_line(x, t, w):
    y = w[0]*x+w[1]
    dw_0 = 2*np.mean((y-t)*x)
    dw_1 = 2*np.mean(y-t)
    return dw_0, dw_1


np.random.seed(seed=1)
n = 16
x = 5+25*np.random.rand(n)

c = [170, 108, 0.2]
t = c[0]-c[1]*np.exp(-c[2]*x)+4*np.random.randn(n)

d_w = dmse_line(x, t, [10, 165])
print(np.round(d_w, 1))

plt.figure(figsize=(4, 4))
wn = 100
wr0 = [-25, 25]
wr1 = [120, 170]
w0 = np.linspace(wr0[0], wr0[1], wn)
w1 = np.linspace(wr1[0], wr1[1], wn)
ww0, ww1 = np.meshgrid(w0, w1)
j = np.zeros((len(w0), len(w1)))

for i in range(wn):
    for k in range(wn):
        j[k, i] = mse_line(x, t, (w0[i], w1[k]))

cont = plt.contour(ww0, ww1, j, 30, colors="black",
                   levels=(100, 1000, 10000, 100000))
cont.clabel(fmt="%1.0f")
plt.grid(True)

W0, W1, DMSE, w_history = fit_line_num(x, t)

print("繰り返し回数 {0}".format(w_history.shape[0]))
print("W=[{0:.6f}, {1:.6f}]".format(W0, W1))
print("DMSE={0:.6f}".format(DMSE[0], DMSE[1]))
print("MSE={0:.6f}".format(mse_line(x, t, [W0, W1])))
plt.plot(w_history[:, 0], w_history[:, 1], ".-", color="gray",
         markersize=10, markeredgecolor="cornflowerblue")
plt.show()
