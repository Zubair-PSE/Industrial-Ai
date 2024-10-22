import sympy as sym
import math
import numpy as np
from sympy.abc import s,t
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
import matplotlib.pyplot as plt
# variables
Kp=0.5
taup=20
taud=10
# Step input
X = 5/s*sym.exp(-taup*s/taud)
# transfer function
G = (Kp/(taup*s+1))
# Calculate response
Y= G*X
# Inverse laplace
x = inverse_laplace_transform(X,s,t)
y = inverse_laplace_transform(Y,s,t)
print ('y')
print (y)
# Generate data for plot
tm= np.linspace(20,25,5)
xs=np.zeros(len(tm))
ys=np.zeros(len(tm))

for i in range(len(tm)):
    xs[i] += x.subs(t,tm[i])
for i in range(len(tm)):
    ys[i] +=y.subs(t,tm[i])
    print (ys[i])
# plotting
plt.figure()
plt.plot(tm,xs,label='x(t)')
plt.plot(tm,ys,label='y(t)')
plt.legend()
plt.xlabel('Time')
plt.show()
           
