G = [[0 for i in xrange(40)] for j in xrange(40)]
def weight2num(s):
    if s=='-':
        return float('inf')
    else:
        return int(s)

for i in range(40):
    G[i]=map(weight2num,raw_input().split(',') )
#for i in range(40):
#    print G[i]
#get all the edges
edges = []
for u in xrange(40):
    for v in xrange(40):
        edges.append((G[u][v],u,v))

#sort the edges
edges.sort()
#initialise the MST
disjointSet = dict([(i,i) for i in xrange(40)])
#print disjointSet

def find(v):
    return disjointSet[v]

def union(u,v):
    newvalue = find(u)
    oldvalue = find(v)
    for v in disjointSet:
        if find(v)==oldvalue:
            disjointSet[v]=newvalue
MST = set()
minweight = 0
for edge in edges:
    weight,u,v = edge
    if find(u)!=find(v):
        MST.add((u,v))
        union(u,v)
        #print u,v,weight
        minweight+=weight
    #if len(MST)==(40):
    #    break


print minweight
print sum([edge[0]  for edge in edges if edge[0]!=float('inf')] )/2 - minweight
