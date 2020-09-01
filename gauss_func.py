import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,200)
y=np.exp(-x**2)

plt.figure(figsize=(4,4))
plt.plot(x,y,color="blue",linewidth=2)

plt.ylim(-0.5,1.5)
plt.xlim(-4,4)
plt.grid(True)

plt.show()