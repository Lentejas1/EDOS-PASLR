import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import sqrt

def lambd(n):
    return ((n*math.pi)/2)**2


def y1(x):
    return 0.5284548125389278277831359544523759333588518942624011207336230954/(-lambd(1))*(2**(1/2))*math.sin(sqrt(lambd(1))*math.log(x))

def y3(x):
    return -0.118969660056965999709836355627767829655450939170666932518376229/(-lambd(3))*(2**(1/2))*math.sin(sqrt(lambd(3))*math.log(x))

def y5(x):
    return 0.0397802053394542469639631084087816853165277321024370705217411068/(-lambd(5))*(2**(1/2))*math.sin(sqrt(lambd(5))*math.log(x))

def y7(x):
    return -0.118969660056965999709836355627767829655450939170666932518376229/(-lambd(7))*(2**(1/2))*math.sin(sqrt(lambd(7))*math.log(x))

def y9(x):
    return 0.0056062177423997189050529464423001346408618603366234596533671840/(-lambd(9))*(2**(1/2))*math.sin(sqrt(lambd(9))*math.log(x))

def y11(x):
    return -0.001347276698055020991060985242784642473786587498568121978447700/(-lambd(11))*(2**(1/2))*math.sin(sqrt(lambd(11))*math.log(x))

def y13(x):
    return 0.0014537062321399805529368934084434275020704698503897613613374195/(-lambd(13))*(2**(1/2))*math.sin(sqrt(lambd(13))*math.log(x))

def y15(x):
    return -0.000223810302199745443787238426220633622764607531821673206394827/(-lambd(15))*(2**(1/2))*math.sin(sqrt(lambd(15))*math.log(x))

def y17(x):
    return 0.0005617338322648945844485534671450647960656613905291475614894834/(-lambd(17))*(2**(1/2))*math.sin(sqrt(lambd(17))*math.log(x))

def y19(x):
    return -0.000019565798787511860125251248594634973810616467223808005453475/(-lambd(19))*(2**(1/2))*math.sin(sqrt(lambd(19))*math.log(x))


def f(x):
    return y1(x) + y3(x) + y5(x) + y7(x)


X = np.arange(1, math.e, 0.01)
Y = np.array([])

for i in range(len(X)):
    Y = np.append(Y, f(X[i]))


fig, ax = plt.subplots()
ax.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
