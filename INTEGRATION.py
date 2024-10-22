from math import *
N=int(input("Enter how many times you want to sum"))
a=float(input("Enter the lower limit"))
b=float(input("Eter upper limit"))
def Integrate(N,a,b):
    def f(s):
        return 1/(s+1)
    value=0
    value2=0
    for n in range(1,N+1):
        value +=f(a+((n-(1/2))*((b-a)/N)))
    value2  = ((b-a)/N)*value
    
    return value2
print("......................")
print("Answer")
print(Integrate(N,a,b))

    
