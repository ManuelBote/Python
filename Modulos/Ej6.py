# Encuentra la raíz de la expresión matemática 𝑥 + 3 + 2 − 8 y muéstrala por pantalla. 
# Encuentra el mínimo de la función matemática 𝑥2 − 10 − 𝑥 y muéstralo por pantalla.

from scipy.optimize import root
from scipy.optimize import minimize

def raiz(x):
    return x+3+2-8

myroot = root(raiz, 0)
print(myroot)

def minimo(x):
    return x**2 - 10 - x

print("==============================================")

mymin = minimize(minimo, 0, method='BFGS')
print(mymin)

