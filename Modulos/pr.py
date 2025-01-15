from scipy.optimize import root
from scipy.optimize import minimize
from math import cos

def ecuacuacion(x):
    return x + cos(x)

def formula(x):
    return x + cos(x)

myroot = root(formula, 0)

def minimo(x):
    return x**2 + x + 2

mymin = minimize(minimo, 0, method='BFGS')
print(mymin)


