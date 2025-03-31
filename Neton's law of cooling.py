import numpy as np
from sympy import *
from matplotlib import pyplot as plt
t2 = 20 # surrounding temp
t1 = 100 # inital temp
# one reading t = 1 minute temp is 75 degree
t = 10
T = 75
k1 = (1/t)*log(( t1 - t2)/(T-t2)) # k calculation
print ('k= ', k1 )
k = Symbol ('k')
t = Symbol ('t')
T = Function ('T')(t)
T = t2 + ( t1 - t2)*exp(-k*t) # solution
print ('T = ',T )
# ploting the solution curve
T=T.subs (k , k1 )
T=lambdify (t , T )
t=np.linspace(0,70)
plt.plot(t,T(t),color='red')
plt.grid ()
plt.show ()
print ('When time t=30 minute T is,',T(30),'o C')