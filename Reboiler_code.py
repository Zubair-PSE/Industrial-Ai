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
F=float(input("Enter F(volumetric flowrate)"))
Ti=float(input("Enter Temp inlet"))
To=float(input("Enter Temp outlet"))

V=20
rho=993
#Cpo=float((3.47*296)+(1.15*(10^3)*296*To))
#Cpi=float((3.47*296)+(1.15*(10^3)*296*Ti))
#Cpavg=float((Cpi+Cpo)/2)
Cpavg=4200
step=To-Ti
#ftime=int(input("Enter Final time"))

Kp=1 #/(F*rho*Cpavg)
taup=V/F
taud=10
#step=60
ftime=60

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
print ('taup',taup)
print ('Kp',Kp)
# Generate data for plot
tm=np.linspace(0,ftime,ftime+1)
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
'''
print ("this is t",tm)
plt.plot(tm,xs,label='x(t)')
plt.plot(tm,ys,label='y(t)')
plt.legend()
animation.FuncAnimation(plt.gfc(),interval=1000)
plt.xlabel('Time')
plt.show()
'''
