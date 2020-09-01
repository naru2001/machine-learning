import numpy as np

def f(a):
    u=sum(np.exp(i) for i in a)
    return [np.exp(i)/u for i in a]

A=[2,1,-1]
y=f(A)
print(np.round(y,2))
print(sum(y))