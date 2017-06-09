"""
Dynamic Programming... start n vs. k the minimum cost is 0. i = k. i = k+1, try k+1. 
dp[i][j] = the minimum cost to forming j heaps with i
"""

n,k = map(int,raw_input().split())
w = [0 for i in xrange(n+1)]
d = [0 for i in xrange(n+1)]
for i in xrange(1,n+1):
    d[i],w[i]= map(int,raw_input().split())

dp = [[0 for i in xrange(k+1)] for j in xrange(n+1)]
lastColumn = [[0 for i in xrange(k+1)] for j in xrange(n+1)]


#initial values
for i in xrange(1,n+1):
    #with just one stack 
    dp[i][1] = dp[i-1][1] + w[i]*(d[i]-d[1])
    lastColumn[i][1] = 1
#for j in xrange(1,k+1):
    #with same number of poles and stacks
#    dp[j][j] = 0
#    lastColumn[j][j] = j



for i in xrange(1,n+1):
    for j in xrange(2,k+1):
        if i<=j:
            #nothing, interesting happens when number of poles less than number of stacks
            #stacks.append(i)
            continue
        if dp[i-1][j-1]<= dp[i-1][j] + w[i]*(d[i] - d[lastColumn[i-1][j]]):
            #print i,j,d[i],d[lastColumn[i-1][j]],w[i]*(d[i] - d[lastColumn[i-1][j]])
            #print dp[i-1][j-1],
            lastColumn[i][j] = i
            #print i
            #stacks.append(lastColumn[i][j])
            dp[i][j] = dp[i-1][j-1]
        else:
            #print dp[i-1][j] + w[i]*(d[i] - d[lastColumn[i-1][j]]),
            lastColumn[i][j] = lastColumn[i-1][j]
            dp[i][j] = dp[i-1][j] + w[i]*(d[i] - d[lastColumn[i-1][j]])
        #print i,j,dp[i][j]
    print i,dp[i]
print dp[n][k]

        