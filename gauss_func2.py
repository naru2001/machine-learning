from ast import fix_missing_locations
import numpy as np
import matplotlib.pyplot as plt


def gauss(mu, sigma, a):
    return a*np.exp(-(x-mu)**2 / (2*sigma**2))


x = np.linspace(-4, 4, 100)
plt.figure(figsize=(4, 4))
plt.plot(x, gauss(0, 1, 1), color="black", linewidth=3)
plt.plot(x, gauss(2, 2, 0.5), color="gray", linewidth=3)
plt.ylim(-0.5, 1.5)
plt.xlim(-4, 4)

plt.grid(True)
plt.show()
