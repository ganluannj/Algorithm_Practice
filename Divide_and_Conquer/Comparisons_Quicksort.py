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
# write a function to count the number of comparisons performed
# for quicksort using the first elements as pivot
def Comparisonsfirst (X, low, high):
    # X is the array needs to be sorted
    if (high<=low): return (0) 
    else:
        # partition with the first element as pivot
        indexp=Partitionfirst(X, low, high)
        # sort the left and right part
        T=high-low
        return (T + Comparisonsfirst(X, low, indexp-1) + Comparisonsfirst(X, indexp+1, high))


#%% 
# test Comparisonfirst
n=15
# A=np.arange(n)
# shuffle(A)
# print(A)
A=[3, 7, 6, 4, 2, 1]
C= Comparisonsfirst(A, low=0, high=(len(A)-1))
print(A)
print(C)


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
# write a function to count the number of comparisons performed
# for quicksort using the first elements as pivot
def Comparisonslast (X, low, high):
    # X is the array needs to be sorted
    if (high<=low): return (0) 
    else:
        # partition with the first element as pivot
        indexp=Partitionlast(X, low, high)
        # sort the left and right part
        T=high-low
        return (T + Comparisonslast(X, low, indexp-1) + Comparisonslast(X, indexp+1, high))


#%% 
# test Comparisonfirst
n=15
# A=np.arange(n)
# shuffle(A)
# print(A)
A=[3, 7, 6, 4, 2, 1]
C= Comparisonslast(A, low=0, high=(len(A)-1))
print(A)
print(C)

#%%
# Quicksort always choose the 'median' element as pivot
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
# write a function to count the number of comparisons performed
# for quicksort using the first elements as pivot
def Comparisonsmedian (X, low, high):
    # X is the array needs to be sorted
    if (high<=low): return (0) 
    else:
        # partition with the first element as pivot
        indexp=Partitionmedian(X, low, high)
        # sort the left and right part
        T=high-low
        return (T + Comparisonsmedian(X, low, indexp-1) + Comparisonsmedian(X, indexp+1, high))


#%% 
# test Comparisonfirst
n=3
A=np.arange(n)
# shuffle(A)
# print(A)
# A=[3, 7, 6, 4, 2, 1]
C= Comparisonsmedian(A, low=0, high=(len(A)-1))
print(A)
print(C)


#%%
# for programming assignment
# comparsionfist
A = loadtxt("QuickSort.txt", unpack=False)
C1 = Comparisonsfirst(A, low=0, high=(len(A)-1))
        
# comparsionlast
A = loadtxt("QuickSort.txt", unpack=False)
C2 = Comparisonslast(A, low=0, high=(len(A)-1))        
        
# comparsionmedian
A = loadtxt("QuickSort.txt", unpack=False)
C3 = Comparisonsmedian(A, low=0, high=(len(A)-1))
