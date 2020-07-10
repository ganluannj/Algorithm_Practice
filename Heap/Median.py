
#%%
# Create class Heap
class Heap():
    
    def __init__(self, MinorMax='Min'):
        # MinorMax is a string either 'Min' or 'Max'
        # indicating whether the Heap is a Min based or Max based Heap
        self.I=MinorMax
        self.vals=[0] # put 0 here to make sure the index of real Heap elements start from 1
    
    def __str__(self):
        return 'This is a '+ self.I + ' based Heap with ' + str(len(self.vals)-1) + ' elements.'
    def Length(self):
        return len(self.vals)-1
    
    def insert(self, x):
        # insert a value to Heap
        # put element at the end of the list
        import math
        self.vals.append(x)
        # bubble up
        if (self.I=='Min'):
            i = len(self.vals)-1
            while (i>1):
                parindex=math.floor(i/2)
                par=self.vals[parindex]
                if (par>self.vals[i]):
                    self.vals[parindex]=self.vals[i]
                    self.vals[i]=par
                    i=parindex
                else:
                    i=1
        else:
            i = len(self.vals)-1
            while (i>1):
                parindex=math.floor(i/2)
                par=self.vals[parindex]
                if (par<self.vals[i]):
                    self.vals[parindex]=self.vals[i]
                    self.vals[i]=par
                    i=parindex
                else:
                    i=1
            
    def MinorMax (self):
        # only return the min or max value, do not delete it
        if len(self.vals)==1:
            raise ValueError ('no values in Heap')
        return (self.vals[1])
    
    def extract(self):
        # if it is a Min based heap, this will return the minimal and delete the minimal from heap
        # if it is a Max based heap, this will return the maximum and delete the maximum from heap
        if len(self.vals)==1:
            raise ValueError ('no values in Heap')
        else:
            Root=self.vals[1]
            if (self.I=='Min'):
                # replace the root with last element, delete the last element
                self.vals[1]=self.vals[-1]
                del self.vals[-1]
                # bubble down
                i=1
                while (2*i <= len(self.vals)-1):
                    Val2i_1 = self.vals[2*i+1] if 2*i+1 <=len(self.vals)-1 else float('inf') 
                    # node i has two kids
                    minindex=2*i if self.vals[2*i]<=Val2i_1 else 2*i+1
                    minvalue=min(self.vals[2*i], Val2i_1)
                    if self.vals[i]>minvalue:
                        temp=self.vals[i]
                        self.vals[i]=self.vals[minindex]
                        self.vals[minindex]=temp
                        i=minindex
                    else:
                        i=len(self.vals)-1
            else:
                # replace the root with last element, delete the last element
                self.vals[1]=self.vals[-1]
                del self.vals[-1]
                # bubble down
                i=1
                while (2*i <= len(self.vals)-1):
                    Val2i_1 = self.vals[2*i+1] if 2*i+1 <=len(self.vals)-1 else float('-inf') 
                    # node i has two kids
                    maxindex=2*i if self.vals[2*i]>=Val2i_1 else 2*i+1
                    minvalue=max(self.vals[2*i], Val2i_1)
                    if self.vals[i]<minvalue:
                        temp=self.vals[i]
                        self.vals[i]=self.vals[maxindex]
                        self.vals[maxindex]=temp
                        i=maxindex
                    else:
                        i=len(self.vals)-1
            
            return Root    
                    

#%%
from numpy import loadtxt
# A = loadtxt("Median_test1.txt", unpack=False)
# A = loadtxt("Median_test2.txt", unpack=False)
A = loadtxt("Median.txt", unpack=False)
Median=[]
# assume A contains more than 2 elemtns
# Low is a Max Heap, while High is a Min Heap
Low=Heap('Max')
High=Heap('Min')
Low.insert(min(A[0],A[1]))
High.insert(max(A[0], A[1]))
Median.append(A[0])
Median.append(min(A[0], A[1]))

for i in range(2, len(A)):
    Lowmax= Low.MinorMax()
    if A[i]<=Lowmax:
        Low.insert(A[i])
    else:
        High.insert(A[i])
    lenlow=Low.Length()
    lenhigh=High.Length()
    if (lenlow==lenhigh):
        Median.append(Low.MinorMax())
    if (lenlow-lenhigh==1):
        Median.append(Low.MinorMax())
    if (lenlow-lenhigh==-1):
        Median.append(High.MinorMax())
    if (lenlow-lenhigh==2):
        High.insert(Low.extract())
        Median.append(Low.MinorMax())
    if (lenlow-lenhigh==-2):
        Low.insert(High.extract())
        Median.append(Low.MinorMax())

print (sum(Median)%10000)   