import time
start = time.time()
n = int(raw_input().strip())
number = raw_input().strip()

#d[n][k][s] stores the number of subsequences starting from n counting from the right. 1 is the rightmost digit
#, with subsequence length k and such that when the 
#subsequence is concatenated to form a number, s is the num%8
d = [[[0 for k in xrange(8)] for j in xrange(4)] for i in xrange(n+1)]

#calculates the values for the case where the subsequence contains just one element
for i in xrange(n):
    for s in xrange(8):
        d[i+1][1][s]=d[i][1][s]
    d[i+1][1][int(number[-i-1])%8]+=1

#calculates the values for the subsequence lengths up to 3
for i in xrange(n):
    for k in xrange(1,min(n,3)):
        for s in xrange(8):
            d[i+1][k+1][s] +=d[i][k+1][s]
            d[i+1][k+1][(int(number[-i-1])*(2**k)+s)%8] +=d[i][k][s]

if n==1:
    print d[n][1][0]
elif n==2:
    print d[n][2][0]+d[n][1][0]
else:
    count = d[n][3][0]+d[n][2][0]+d[n][1][0]
    #print d[n][1][0], d[n][2][0],d[n][3][0]
    #Only the last three digits need to be divisible by 8 for the number to be divisble by 8 
    for m in xrange(4,n+1):
        count+=pow(2,n-m,1000000007)*d[m-1][3][0]
    print count%1000000007

print time.time()-start