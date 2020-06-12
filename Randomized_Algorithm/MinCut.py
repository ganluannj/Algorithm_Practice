import numpy as np
Data=[]
with open('kargerMinCut.txt') as f:
    for line in f:
        temp=[int(v)-1 for v in line.split()]
        temp=np.reshape(temp, (1,len(temp)))
        Data.append(temp)
# preprocessing data to a graph format
# the graph is store in a list G
# each element of list  G, say G[i],store info about ith vertex
# G[i] is a list with two elements
# the first element of G[i] is a list containing vertices (contracted vertices)
# the second element of G[i] is the vertices connected to this vertex
# after contraction, contracted vertices are all represented by one vertex
# represented by G[i][0][0], first element of list containing vertices
# for the algorithm of randomized contraction algorithm, we allowed G[i] containing two empty list
Gtest=[]
for data in Data:
    list1=np.array([data[0,0]])
    list2=np.array([])
    if len(data[0])>1:
        list2=data[0, 1:]
    Gtest.append([list1, list2])
    

#%%
# write a function to count number of vertices
def Vcount (G):
    # G is a graph, allow elemnts to be empty lists
    count=np.sum([len(g[0])>0 for g in G])
    return (count)

# write a function to count the number of edges
# actually the return result is two times of the number of edges
def Ecount (G):
    # G is a graph, allow elemnts to be empty lists
    count=np.sum([len(g[1]) for g in G])
    return (count)

# write a fucntion to randomly return a edge of G
# return indeices of two vertices for this edge with the smaller one be the first
def Gselect(G):
    import random
    T=Ecount(G)
    # random select a integer from 0 to T-1
    t=random.randint(0, T-1)
    # get the corresponding edge
    if t==0: 
        u=G[0][0][0]
        v=G[0][1][0]
    else:
        count=0
        for i in range(len(G)):
            if count<t and len(G[i][0]):
                Lastcount=count # this is the largest count less than T
                Fline=i # edge we want is in this line
                count+=len(G[i][1])
        g=G[Fline]
        u=g[0][0]
        v=g[1][t-Lastcount-1]
    
    return ((min(u,v), max(u,v)))
            
    
    
#%%
# write a function to contract two vertices
def Contract(G, u, v):
    # G is the graph
    # u, v are indices for two vertices to be contracted
    # u<v
    import numpy as np
    # first change vertex v to u in all edges
    for i in G[v][1]:
        G[i][1][G[i][1]==v]=u
    # copy all edges in v to u
    G[u][1]=np.append(G[u][1], G[v][1])
    # remove self-loop
    G[u][1]=np.delete(G[u][1], np.where (G[u][1]==u))
    # copy vertex v to u 
    G[u][0]=np.append(G[u][0], G[v][0])
    # make the list according to v to be empty list
    G[v]=[np.array([]), np.array([])]
    
#%%
# get the cut
def Cut(G):
    # get cut from graph G
    # need to make sure G only have two  vertices
    assert Vcount(G)==2, 'number of vertices is not 2'
    # one of these two left vertices must be the first vertices
    v1=G[0][0]
    v2=np.array([])
    i=1
    while len(v2)==0:
       v2=G[i][0]
       i+=1
    return v1, v2

#%%
# count cross for a cut
def Crosscount(G, v1, v2):
    # G is the original graph without any contraction
    # v1 and v2 are two seperates groups
    cross=0
    for i in v1:
        cross+=len([val for val in G[i][1] if val in v2])
    return cross
#%%
def RContractsingle (G):
    # a function to run one round of randomized contraction
    # to find the minimum cut
    # return cross and two seperate group in a dictionary
    # three elements in the dictionary
    # "cross" number of crosses
    # "A", "B": two groups
    from copy import deepcopy
    assert Ecount(G)>=2, 'graph only has one vertex'
    # first copy G 
    F = deepcopy(G)
    # print (G)
    LEN=Vcount(F)
    while LEN>2:
        # select one edge
        u, v = Gselect (F)
        # contract two vertices
        Contract(F, u, v)
        LEN-=1
    # get the cut
    A,B = Cut(F)
    # count cross
    cross=Crosscount(G, A, B)
    Result={'cross':cross, 'A':A, 'B':B}
    return (Result)
   
#%%    
# write a function perform Randomized contraction
# to find the minimum cut
# return the smallest cross found 
# and also the corresponding cuts
def MinCut(G, N):
    # G is a connected graph
    # N is total number of RContractsingle
    mincross=Ecount(G)
    for i in range(N):
        Temp=RContractsingle(G)
        if Temp['cross'] < mincross:
            mincross=Temp['cross']
            FinalA=Temp['A']
            FinalB=Temp['B']
    Cuts=[]
    for i in FinalA:
        for j in G[i][1]:
            if j in FinalB:
                Cuts.append((i,j))
                
    return {'cross':mincross, 'Cuts': Cuts}
    


#%%
Gf=[]
Gf.append([np.array([0]), np.array([1,2])])
Gf.append([np.array([1]), np.array([0,2,3])])
#G.append([[], np.array([])])
Gf.append([np.array([2]), np.array([0,1,3])])
Gf.append([np.array([3]), np.array([1,2])])

#%%
Gf=[]
Gf.append([np.array([0]), np.array([1,2,3,6])])
Gf.append([np.array([1]), np.array([0,2,3])])
Gf.append([np.array([2]), np.array([0,1,3])])
Gf.append([np.array([3]), np.array([0,1,2,4])])
Gf.append([np.array([4]), np.array([3,5,6,7])])
Gf.append([np.array([5]), np.array([4,6,7])])
Gf.append([np.array([6]), np.array([0,4,5,7])])
Gf.append([np.array([7]), np.array([4,5,6])])
#%%
n=Vcount(Gf)
N=int(np.floor(n*n*np.log(n)))
Result=MinCut(Gf,N)
Result['cross']
Result['Cuts']    
#%% 
# run the assignment
n=Vcount(Gtest)
N=int(np.floor(n*n*np.log(n)))
import time
start=time.time()
Result=MinCut(Gtest,1000)
print(time.time()-start)
Result['cross']
Result['Cuts']    

