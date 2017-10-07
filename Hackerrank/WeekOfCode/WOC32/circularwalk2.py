import sys
import time
start = time.time()
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    dp=[float('inf')]*n
    R = [0]*n 
    R[0]=r_0
    for i in range(1,n):
        R[i]=(R[i-1]*g+seed)%p
    #print R
    time=0
    stack=[(s,0)]
    u = s,0
    visited=[False]*n
    visited[s]=True
    while stack and u!=t:
        u,time = stack.pop(0)
        print u,time
        visited[u]=True
        if R[u]==0:
            continue
        
        if not visited[(u+v)%n]: #
            
            stack.append(((u-R[u])%n , time+1))
            dp[(u-R[u])%n]=min(dp[(u-R[u])%n],time+1)
            
            stack.append(((uR[u]+1)%n , time+1))
            dp[(u+R[u])%n]=min(dp[(u+R[u]+1)%n],time+1)
    return min(dp[(u+R[u])%n],dp[(u-R[u])%n])

n, s, t = raw_input().strip().split(' ')
n, s, t = [1000 ,1, 345]#[int(n), int(s), int(t)]
r_0, g, seed, p = [1,4,5,91]#raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
print time.time()-start