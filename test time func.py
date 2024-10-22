import sympy as sym
import math
import numpy as np
from sympy.abc import s,t
#from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
import matplotlib.pyplot as plt
import time
import datetime as dt
import matplotlib.animation as animation
# variables
#Kp=float(input("Enter Kp"))
#taup=float(input("Enter taup"))
#taud=float(input("Enter taud"))
#step=float(input("Enter step change"))
#ftime=int(input("Enter Final time"))

Kp=0.5
taup=20
taud=10
step=5
ftime=30

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
newTime= time.clock()
tm=np.append(tm,newTime)
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

print ("this is t",tm)
plt.plot(tm,xs,label='x(t)')
plt.plot(tm,ys,label='y(t)')
plt.legend()
animation.FuncAnimation(plt.gfc(),interval=1000)
plt.xlabel('Time')
plt.draw()

