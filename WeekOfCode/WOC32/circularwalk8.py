import time
from heapq import *
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    dp = [-1]*n
    #print n,dp,range(n)
    dp[s]=0
    queue = [(0,s)]
    heapify(queue) #replace with makequeue
    while queue:
        distance,u=heappop(queue) #remove the item with the least value
        #print u
        for d in xrange(-R[u],R[u]+1):
            if dp[(u+d)%n]==-1: # I need a measure of distance between two points simply abs(s-t) and (n-abs(s-t))%n
                dp[(u+d)%n]=dp[u]+1
                heappush(queue,(dp[(u+d)%n],((u+d)%n)))
                if t==(u+d)%n:
                    return dp[(u+d)%n]
    if dp[t]!=-1:
        return dp[t]
    else:
        return -1


start = time.time()

n, s, t = 1000000,0,500000#raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = 1, 3, 4, 7#raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]

visited=[False]*n
R = [0]*n 
R[0]=r_0
for i in range(1,n):
    R[i]=(R[i-1]*g+seed)%p

#print R

result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
print time.time()-start