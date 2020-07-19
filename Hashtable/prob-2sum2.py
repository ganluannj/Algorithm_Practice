#%%
import numpy as np
from numpy import loadtxt
# A = loadtxt("prob-2sum-test1.txt", unpack=False)
Numbers= loadtxt("prob-2sum.txt", unpack=False)
print('data reading done')
#%%
# sort Numbers
# remove numebr that is not possible to contribute to the sum
Numbers.sort()
i=0
j=len(Numbers)-1
Sums=[]
while(i<j):
    if (Numbers[i]+Numbers[j]>10000):
        j=j-1
    elif (Numbers[i]+Numbers[j]<-10000):
        i=i+1
    else:
        k=i
        S=Numbers[k]+Numbers[j]
        while (S<=10000):
            Sums.append(S)
            k=k+1
            S=Numbers[k]+Numbers[j]
        i=i+1  
        j=j-1
SumU=np.unique(Sums)
print(len(SumU))