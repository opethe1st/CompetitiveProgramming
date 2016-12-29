n = input()
A = map(int,raw_input().split())

dp = [0]*(n+1)

prefixsum = [0]*(n+1)
for i in xrange(0,n):
    prefixsum[i+1]= (A[i]*2**(i)+prefixsum[i])%1000000007

for i in xrange(1,n+1):
    dp[i]= (2*dp[i-1]+prefixsum[i-1]+(2**i-1)*A[i-1] ) %1000000007

print dp[-1] 