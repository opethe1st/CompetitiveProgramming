import time
start = time.time()
dp = [[-1 for i in xrange(2)] for j in xrange(51)]
RED = 1
BLACK = 0

#initialises
dp[0][BLACK]=0
dp[1][BLACK]=1
dp[2][BLACK]=1
dp[3][BLACK]=1

dp[0][RED]=0
dp[1][RED]=0
dp[2][RED]=0
dp[3][RED]=1

def f(n,colour):
    if dp[n][colour]!=-1:
        return dp[n][colour]
    else:
        s = 0
        if colour==RED:
            for i in xrange(n-2):
                s+=f(i,BLACK)
            dp[n][colour]=s+1
            return s+1
        else:
            for i in xrange(n):
                s+=f(i,RED)
            #dp[n][colour]=s+1
            return s+1

print f(30,RED)+f(50,BLACK)
print time.time()-start