# Enter your code here. Read input from STDIN. Print output to STDOUT
import time
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    dp = [-1]*n
    dp[s]=0
    queue=[s]
    i = 0
    nitems=1
    while i<nitems:
        u=queue[i]
        if R[u]==0:
            i+=1
            continue
      
        for d in xrange(1,R[u]+1):
            if u+d>=n:
                v=u+d-n
            else:
                v = u+d
            if dp[v]==-1: #tells us if a node has been visited before or not
                nitems+=1
                queue.append(v)
                dp[v]=dp[u]+1
                if t==v:
                    return dp[t]
            if u<d:
                v=n+u-d
            else:
                v=u-d
            if dp[v]==-1: #tells us if a node has been visited before or not
                nitems+=1
                queue.append(v)
                dp[v]=dp[u]+1
                if t==v:
                    return dp[t]
        i+=1
    return dp[t]
    


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