import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import sqrt


with open("b_n.txt", "r") as file:
    b = [_.rstrip('\n') for _ in file.readlines()]

X = np.arange(1, math.e, 0.01)
Y = np.array([])
N = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

for x in range(len(X)):
    f = 0.
    a = X[x]
    for i in range(10):
        lambd = ((N[i] * math.pi) / 2) ** 2
        f += (float(b[i])) * sqrt(2) * math.sin((N[i] * math.pi / 2) * math.log(a)) / (-lambd)
    Y = np.append(Y, f)

fig, ax = plt.subplots()
ax.plot(X, Y)

plt.xlabel("x")
plt.ylabel("y")
plt.show()
