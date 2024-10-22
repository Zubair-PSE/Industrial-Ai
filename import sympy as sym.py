from turtle import clear
import sympy as sym
from sympy.abc import s,t
from sympy.integrals import laplace_transform
from sympy.integrals import inverse_laplace_transform
Y= laplace_transform(5*t,t,s)
print(Y[0])
clear