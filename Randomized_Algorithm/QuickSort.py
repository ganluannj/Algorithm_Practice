from numpy import loadtxt
import numpy as np
from random import shuffle


#%%
# Quicksort always choose the first element as pivot

# first write a function for partition
def Partitionfirst (X, l, r):
    # l and r are indices for X
    # we want to partition X[l:r} about pivot p=X[l]
    # after partition all elements left to p is smaller than p 
    # and all elements right to p is larger than p 
    # also current location of pivot
    if l>=r: return (l)
    else:
        p=X[l]
        i=l+1
        for j in range(l+1, r+1):
            # do nothing if A[j]>p
            if X[j]<p:
                # swap A[j] with the left most element greater than p, which is A[i]
                temp=X[j]
                X[j]=X[i]
                X[i]=temp
                i=i+1
        # swap A[l] and A[i-1]
        temp=X[i-1]
        X[i-1]=X[l]
        X[l]=temp
        return (i-1)

#%%
def Quicksortfirst (X, low, high):
    # X is the array needs to be sorted
    if (high>low):
        # partition with the first element as pivot
        indexp=Partitionfirst(X, low, high)
        # sort the left and right part
        Quicksortfirst(X, low, indexp-1)
        Quicksortfirst(X, indexp+1, high)


#%% 
# test Quicksortfirst
n=50
A=np.arange(n)
shuffle(A)
print(A)
Quicksortfirst(A, low=0, high=(len(A)-1))
print(A)

#%%
# Quicksort always choose the last element as pivot

# first write a function for partition
def Partitionlast (X, l, r):
    # l and r are indices for X
    # we want to partition X[l:r} about pivot p=X[r]
    # after partition all elements left to p is smaller than p 
    # and all elements right to p is larger than p 
    # also current location of pivot
    if l>=r: return (l)
    else:
        # first swap X[l] with X[r]
        temp=X[l]
        X[l]=X[r]
        X[r]=temp
        # let the first element be pivot
        p=X[l]
        i=l+1
        for j in range(l+1, r+1):
            # do nothing if A[j]>p
            if X[j]<p:
                # swap A[j] with the left most element greater than p, which is A[i]
                temp=X[j]
                X[j]=X[i]
                X[i]=temp
                i=i+1
        # swap A[l] and A[i-1]
        temp=X[i-1]
        X[i-1]=X[l]
        X[l]=temp
        return (i-1)

#%%
def Quicksortlast (X, low, high):
    # X is the array needs to be sorted
    if (high>low):
        # partition with the first element as pivot
        indexp=Partitionlast(X, low, high)
        # sort the left and right part
        Quicksortlast(X, low, indexp-1)
        Quicksortlast(X, indexp+1, high)


#%% 
# test Quicksortlast
n=50
A=np.arange(n)
shuffle(A)
print(A)
Quicksortlast(A, low=0, high=(len(A)-1))
print(A)


#%%
# Quicksort always choose the median element as pivot

# first write a function for partition
def Partitionmedian (X, l, r):
    # l and r are indices for X
    # we want to partition X[l:r} about pivot p=X[l]
    # after partition all elements left to p is smaller than p 
    # and all elements right to p is larger than p 
    # also current location of pivot
    import numpy as np
    if l>=r: return (l)
    else:
        if (r-l>=2):
            # get index of median elements
            Indices=[l, r, int(np.floor(l+r)/2)]
            Elements=np.array([X[l], X[r], X[int(np.floor(l+r)/2)]])
            index, = np.where (Elements==np.sort(Elements)[1])
            index=index.item()
            medianindex=Indices[index]
            # swap medianindex and l 
            temp=X[l]
            X[l]=X[medianindex]
            X[medianindex]=temp
        
        p=X[l]
        i=l+1
        for j in range(l+1, r+1):
            # do nothing if A[j]>p
            if X[j]<p:
                # swap A[j] with the left most element greater than p, which is A[i]
                temp=X[j]
                X[j]=X[i]
                X[i]=temp
                i=i+1
        # swap A[l] and A[i-1]
        temp=X[i-1]
        X[i-1]=X[l]
        X[l]=temp
        return (i-1)

#%%
def Quicksortmedian (X, low, high):
    # X is the array needs to be sorted
    if (high>low):
        # partition with the first element as pivot
        indexp=Partitionmedian(X, low, high)
        # sort the left and right part
        Quicksortmedian(X, low, indexp-1)
        Quicksortmedian(X, indexp+1, high)


#%% 
# test Quicksortfirst
n=15
A=np.arange(n)
shuffle(A)
print(A)
Quicksortmedian(A, low=0, high=(len(A)-1))
print(A)
        
        