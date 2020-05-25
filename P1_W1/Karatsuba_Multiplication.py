
# define a truncate function to truncate the integer
# to make the last k digits to be zeros
def truncate(n, k):
    multiplier = 10 ** (-k)
    return int(int(n * multiplier) / multiplier)


def Karatsuba (x,y):
    import numpy as np
    from math import ceil, log
    # use the Karatsuba multiplication to calculate the 
    # product of two integers
    x=int(x)
    y=int(y)
    if len(str(abs(x)))==1 or len(str(abs(y)))==1: return (x*y)
    else:
        n=len(str(abs(x)))
        m=len(str(abs(y)))
        n1=int(np.floor(n/2))
        m1=int(np.floor(m/2))
        a=truncate(x, n-n1)
        b=x-a
        a=int(a/(10**n1))
        c=truncate(y, m-m1)
        d=y-c
        c=int(c/(10**m1))
        ac=Karatsuba(a,c)
        ad=Karatsuba(a,d)
        bc=Karatsuba(b,c)
        bd=Karatsuba(b,d)
        S=10**(n1+m1)*ac+10**n1*ad+10**m1*bc+bd
        return(S)
        
    
# test the function
import random
Range=10000000
Iters=3000
index=1
for i in range(Iters):
    a=random.randint(-Range, Range)
    b=random.randint(-Range, Range)
    P=Karatsuba(a,b)
    if (P-a*b!=0): 
        print('Wrong')
        print('a= ', a)
        print('b= ', b)
        index=0
if index: print('all correct')
