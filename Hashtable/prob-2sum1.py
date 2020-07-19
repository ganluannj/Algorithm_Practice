#%%
import numpy as np
from numpy import loadtxt
# A = loadtxt("prob-2sum-test1.txt", unpack=False)
A= loadtxt("prob-2sum.txt", unpack=False)
print('data reading done')
#%%
#define the hash function
HT={}
for a in A:
    HT[a]=a
print('hash table done')
#%%
Keys=[*HT]
L=len(Keys)
#%%
T=np.arange(-10000,10001)
#%%
count=0
for t in T:
    index=0
    while (index<L):
        x=HT[Keys[index]]
        index=index+1
        if ((HT.get(t-x)!=None) and (HT.get(t-x)!=x)):
            count = count +1
            index=L
    if (t%1000==0):
        print (t)
        
print ('the final count is', count)   

