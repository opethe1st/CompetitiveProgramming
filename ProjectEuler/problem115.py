import time
start = time.time()
dp = [[-1 for i in xrange(2)] for j in xrange(5000)]
RED = 1
BLACK = 0

#initialises
dp[0][BLACK]=0
for i in xrange(1,51):
    dp[i][BLACK]=1

for i in xrange(50):
    dp[i][RED]=0

dp[50][RED]=1
#print dp[5][BLACK]
def f(n,colour):
    if dp[n][colour]!=-1:
        return dp[n][colour]
    else:
        s = 0
        if colour==RED:
            for i in xrange(n-49):
                s+=f(i,BLACK)
            dp[n][colour]=s+1
            return s+1
        else:
            for i in xrange(n):
                s+=f(i,RED)
            dp[n][colour]=s+1
            return s+1
s = f(50,RED)+f(50,BLACK)
i = 50
while s<10**6:
    i+=1
    s= f(i,RED)+f(i,BLACK)
print s,i
print time.time()-start