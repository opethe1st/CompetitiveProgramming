"Find the length of the longest (strictly) increasing subsequence"

a = [2,1,4,7,3,2,10,9,11,10,13,2,11]
n = len(a)
dp = [0]*n 

for i in xrange(n):
    mx = 0
    for j in xrange(i):
        if (a[j]<a[i] and mx<dp[j]):
            mx = dp[j]
    dp[i]=mx+1

print max(dp)

"It works!!"