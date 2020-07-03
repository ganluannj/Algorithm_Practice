#%%
import numpy as np
import pandas as pd
# sys.setrecursionlimit(800000)
# threading.stack_size(67108864)
#%%
def DFS(G, i):
    # G is the graph, i the initial node, j is the node we search for
    # mark i as explored
    global f, t, Explored, leader, s
    import numpy as np
    if i in Explored:
        return 
    print (i)
    Explored=np.append(Explored, i)
    leader[i]=s
    # get the edges nodes for i
    inodes=G[i][1]
    for node in inodes:
        if not node in Explored:
            DFS(G, node)
    t+=1
    f[i]=t

#%%
L=875714
Gtestrev=[]
for k in range(L):
    Gtestrev.append([[k],[]])
with open('SCC.txt') as ff:
    for line in ff:
        temp=[int(v)-1 for v in line.split()]
        temp=np.reshape(temp, (2,))
        Gtestrev[temp[1]][1].append(temp[0])

print('reading reverse done! ')
print()
#%%
# Global variable
Explored=np.array([], dtype=int)
f=np.zeros(L, dtype=int)
t=-1
leader=np.zeros(L, dtype=int)
s=8
# reverse the original graph 
for i in np.arange(L-1,-1,-1):
    DFS(Gtestrev, i)
del Gtestrev
print ('first round of DFS done!')
print ()
#%%
Gtest=[]
for k in range(L):
    Gtest.append([[k],[]])
with open('SCC.txt') as ff:
    for line in ff:
        temp=[int(v)-1 for v in line.split()]
        temp=np.reshape(temp, (2,))
        Gtest[temp[0]][1].append(temp[1])
print('reading forward done!')
print()
#%%
Explored=np.array([], dtype=int)
t=-1
leader=np.zeros(L, dtype=int)
# create a dataframe to get the order to run nodes
DF=pd.DataFrame({'Order':np.arange(L), 'f':f})
DF=DF.sort_values(by='f', ascending=False)
f=np.zeros(L, dtype=int)
# run on original graph
for k in DF['Order']:
    if not k in Explored:
        s=k
        DFS(Gtest, k)
print('second round of DFS done!')
#%%
# get unique number in leader
Unique=np.unique(leader)
for value in Unique:
    print (np.count_nonzero(leader==value))