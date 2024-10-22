import sympy as sym
import math
import numpy as np
from sympy.abc import s,t
#from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
import matplotlib.pyplot as plt
import time
# variables
Kp=float(input("Enter Kp"))
taup=float(input("Enter taup"))
taud=float(input("Enter taud"))
step=float(input("Enter step change"))
ftime=int(input("Enter Final time"))

# Step input
X = step/s *sym.exp(-taup*s/taud)

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
tm= np.linspace(0,ftime,ftime+1)
xs=np.zeros(len(tm))
ys=np.zeros(len(tm))
for i in range(len(tm)):
    if i <=taud:
        tm[i]=0
    xs[i] +=x.subs(t,tm[i])
    ys[i] +=y.subs(t,tm[i])
    #time.sleep(2)
    print ("This is x", xs[i],"This is y",ys[i])
    
# plotting
tm= np.linspace(0,ftime,ftime+1)
print ("this is t",tm)
plt.plot(tm,xs,label='x(t)')
plt.plot(tm,ys,label='y(t)')
plt.legend()
plt.xlabel('Time')
plt.show()
