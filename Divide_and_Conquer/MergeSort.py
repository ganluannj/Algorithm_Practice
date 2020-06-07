import numpy as np

def merge_sort(X):
    # X is a an array needs to be sorted
    # base case
    m=len(X)
    if m<2: return(X)
    else:
        # divide X into two parts
        Mid=int(np.floor(m/2))
        # sort each part
        X1=merge_sort(X[0:Mid])
        X2=merge_sort(X[Mid:m])
        # merge them together
        R=np.zeros(m)
        i=0;j=0
        for k in range(m):
            if i>=Mid and j < (m-Mid):
                R[k]=X2[j]
                j+=1
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
        return(R)

A=np.arange(60)                
np.random.shuffle(A)        
print(merge_sort(A))
