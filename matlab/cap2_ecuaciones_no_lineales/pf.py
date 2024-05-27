import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()

print("X0:")
X0 = float(input())
print("Tol:")
Tol = float(input())
print("Niter:")
Niter = float(input())
print("Function:")
Fun = input()
print("Function g:")
g = input()

fn=[]
xn=[]
E=[]
N=[]
x=X0
f=eval(Fun)
c=0
Error=100               
fn.append(f)
xn.append(x)
E.append(Error)
N.append(c)
while Error>Tol and f!=0 and c<Niter:
	x=eval(g)
	fe=eval(Fun)
	fn.append(fe)
	xn.append(x)
	c=c+1
	Error=abs(xn[c]-xn[c-1])
	N.append(c)
	E.append(Error)	
if fe==0:
    s=x
    print(s,"es raiz de f(x)")
elif Error<Tol:
    s=x
    print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
    print("N",N)
    print("xn",xn)
    print("fn",fn)
    print("Error",E)
else:
    s=x
    print("Fracaso en ",Niter, " iteraciones ") 


