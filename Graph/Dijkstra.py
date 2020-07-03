#%%
# read data
import numpy as np
Data=[]
with open('dijkstraData.txt') as ff:
    for line in ff:
        temp=[v for v in line.split()]
        temparray=np.array([int(temp[0])-1])
        for i in range(1, len(temp)):
            temparray=np.append(temparray, int(temp[i].split(',')[0])-1)
            temparray=np.append(temparray, int(temp[i].split(',')[1]))
        Data.append(temparray)
#%%        
# Dijkstra's algorithm
def Dijkstra (G, s):
    # G is the graph in a list
    # s is the initial vertex
    # return a array with each element be the length of shortest path
    # for the corresponding vertex
    # if there is no path between vertex n and vertex 1
    # let the distance be 1000000
    import numpy as np
    # get the total number of vertices
    N=len(G)
    # initialize array for shortest length
    A=np.ones(N)*1000000
    A[s]=0
    # initialize the list for vertex that has been explored and not explored
    X=[s]
    V_X=[t for t in range(N)]
    V_X.remove(s)
    # indicator that wheter there is edges cross X and V_X
    vstar=s
    wstar=s
    while len(X)<N:
        # first go through every vertex in X
        Min=1000000
        for v in X:
            temp=G[v]
            K=len(temp)//2
            for k in range(1,K+1):
                if temp[2*k-1] in V_X and A[v]+temp[2*k]<Min:
                    Min=A[v]+temp[2*k]
                    vstar=v
                    wstar=temp[2*k-1]
        if Min==1000000:
            # no cross edges
            break 
        # move wstar to X
        X.append(wstar)
        V_X.remove(wstar)
        # get the lenth of path for wstar
        A[wstar]=Min
            
    return A

#%%
A=Dijkstra(Data, 0)
Index=np.array([7,37,59,82,99,115,133,165,188,197])-1
print(A[Index])