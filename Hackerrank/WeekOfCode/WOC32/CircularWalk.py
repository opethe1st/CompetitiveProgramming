

n, s, t = raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]
#result = circularWalk(n, s, t, r_0, g, seed, p)
#print(result)

R = [-1]*n 
R[0]=r_0
for i in range(1,n):
    R[i]=(R[i-1]*g+seed)%p

#print R
dp=[float('inf')]*n
dp[t]=0
cache = {}
cache[t]=0
def solution(s,path):
    global cache
    #print s,level
    if s==t:
        return 0
    #if s in cache:
    #    return cache[s]

    mini = float('inf')
    for d in xrange(-R[s],R[s]+1):
        if (s+d)%n in path:
            continue
        else:
            path.add((s+d)%n)
            mini=min(mini, solution((s+d)%n,path))
            path.remove((s+d)%n)

    #print s,mini,path
    cache[s]=mini+1
    return mini+1
dp=[float('inf')]*n
dp[s]=0
def solution2(n):
    for i in xrange(s,n):
        for d in xrange(-R[i],R[i]+1):
            dp[(i+d)%n]=min(dp[i]+1,dp[(i+d)%n])
        print dp
    
print R
solution2(n)

print dp[t]

#print cache
