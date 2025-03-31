import sympy as sp
from math import inf
x=sp.symbols('x')
l=sp.Limit((1+1/x)**x,x,inf).doit()
print(l)
