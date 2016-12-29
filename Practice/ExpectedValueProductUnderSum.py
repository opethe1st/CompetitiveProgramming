
MAXN = 100
MAXM = 100
MAXDICE = 6
S= [[0 for i in xrange(MAXM)] for j in xrange(MAXN)]

#base case.. initial values
for i in xrange(1,MAXDICE+1):
    S[1][i]=i #n=1 and m = i

#Compute the table of values of S
for n in xrange(2,MAXN):
    for m in xrange(2,MAXM):
        total = 0
        for i in xrange(1,MAXDICE+1): # this is the summation part
            if n-1>0 and m-i>0: #if not, it goes out of bounds
                total+=i*S[n-1][m-i]
        S[n][m]=total 

print 'Some tests for S'
print S[2][12] #only one possible possible -- dice 1 is 6 and dice 2 is 6.. to give product 36
print S[2][13] #no possible product
print S[2][2] #just one possible product. dice 1 is 1 and dice 2 is 1.. to give product 1
print S[2][1] # should be zero
print S[2][6] #calculated by hand.. it should be 35
print S[8][24] #the sum of the product of eight numbers such that the numbers sum to 24


#Counts the number of products... 
N = [[0 for i in xrange(MAXM)] for j in xrange(MAXN)]
for i in xrange(1,7):
    N[1][i] = 1

for n in xrange(2,MAXN):
    for m in xrange(2,MAXM):
        total = 0
        for i in xrange(1,MAXDICE+1): 
            if n-1>0 and m-i>0: #if not, it goes out of bounds
                total+=N[n-1][m-i]
        N[n][m]=total
print 'Some tests for N'
print N[2][12] #Should be 1
print N[2][13] #should be 0
print N[2][1] #should be 0
print N[2][2] #should be 1
print N[2][6] #should be 5
print N[8][24] 

#Expected value is S[n][m]/N[n][m]

print "the expected value for the product of n numbers (n=8 in this case) such that the sum is m (m=24 in this case) is",S[8][24]/float(N[8][24])
#Is there a way to get a closed form formula that depends on just n and m?