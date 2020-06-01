from numpy import loadtxt
import numpy as np
A = loadtxt("IntegerArray.txt", unpack=False)

def Inversion(X):
    # X is a an array needs to be sorted
    # base case
    # return the count of inversions and 
    # and also sorted array
    m=len(X)
    if m<2: return(0,X)
    else:
        count=0
        # divide X into two parts
        Mid=int(np.floor(m/2))
        # sort each part
        count1, X1=Inversion(X[0:Mid])
        count2, X2=Inversion(X[Mid:m])
        count+=count1+count2
        # merge them together and count the inversions
        R=np.zeros(m)
        i=0;j=0
        for k in range(m):
            if i>=Mid and j < (m-Mid):
                R[k]=X2[j]
                j+=1 # elements in X1 is small
            if i<Mid and j >= (m-Mid):
                R[k]=X1[i]
                i+=1
            if i < Mid and j < (m-Mid):
                if X1[i]<X2[j]:
                    R[k]=X1[i]
                    i+=1
                else:
                    R[k]=X2[j]
                    j+=1
                    count+=Mid-i
        return(count,R)

 
a,b=Inversion(A)
print(a)

