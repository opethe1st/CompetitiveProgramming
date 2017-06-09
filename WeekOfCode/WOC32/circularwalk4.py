import time

def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    queue=[s]
    i = 0
    maxRight=s
    maxLeft=s
    while queue:
        u=queue.pop(0)
        #maxRight=u
        #maxLeft=u
        print 'u',u
        if R[u]==0:
            continue
        for v in xrange(maxRight,R[u]+u+1):
            #v = u+d
            if v<0:
                v+=n
            elif v>=n:
                v-=n
            if dp[v]==-1: #tells us if a node has been visited before or not
                #maxRight=max(maxRight,v)
                queue.append(v%n)
                dp[v%n]=dp[u]+1
                if t==v:
                    return dp[t]
        maxRight=max(maxRight,R[u]+u)
        for v in xrange(u-R[u],maxLeft):
            #v = u-d
            if v<0:
                v+=n
            elif v>=n:
                v-=n
            if dp[v]==-1: #tells us if a node has been visited before or not
                #maxLeft=min(maxLeft,v)
                queue.append(v%n)
                dp[v%n]=dp[u]+1
                if t==v:
                    return dp[t]
        maxLeft=min(maxLeft,u-R[u])
        print maxLeft,maxRight
    return dp[t]
    


start = time.time()

n, s, t = [13, 0, 2]#raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = [1, 3, 4, 7]#raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]

visited=[False]*n
R = [0]*n 
R[0]=r_0
for i in range(1,n):
    R[i]=(R[i-1]*g+seed)%p

#print R
dp = [-1]*n
dp[s]=0
print time.time()-start
result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
print time.time()-start