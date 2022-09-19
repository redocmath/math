def gcd(a, b):
    if (a == 0): return b
    return gcd(b%a, a)
 
def phi(n):
    res = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            res += 1
    return res

def func(A, B):
    return (-2*(A**phi(B)))%(A*B)

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

rng = 100


for a in range(1, rng+1):
    for b in range(1, rng+1):
        res = func(a,b)
        if res <= (2*a*b)**0.5 and res != 0 and res != a*2 and res != a:
            ax.scatter(a, b, res)
            print("(", a, ",", b, ",", res, ")", sep="")

# X = np.arange(1, rng+1, 1)
# Y = np.arange(1, rng+1, 1)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X*Y)

# surf = ax.plot_surface(X, Y, R, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)

plt.show()