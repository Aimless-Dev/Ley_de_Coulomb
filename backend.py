import math

def magnitudYvector(i, j):
    Rx = x[i] - x[j]
    Ry = y[i] - y[j]
    R = math.sqrt((Rx**2) + (Ry**2))
    m = (Rx**2) + (Ry**2) 
    V.append(Rx/R)
    V.append(Ry/R)
  
    return fueza(m, i, j)

def fueza(m, i, j):
    fuerza.clear()
    F = K * (((peso[j]*10**-16)*(peso[i]*10**-16)) / m)
    f1 = (F * V[j])
    f2 = (F * V[i])
    fuerza.append(f1)
    fuerza.append(f2)
    FN.append(fuerza[0])
    FN.append(fuerza[1])
    return f' Fuerza es igual a \n{fuerza} [N]'

K = 9*(10**9)
peso = []
x = []
y = []
R = 0
V = []
fuerza = []
res = 's'
c = 2
FN = []
FF = []
