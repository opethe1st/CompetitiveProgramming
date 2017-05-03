import time
start = time.time()
cache = dict()
LeastPrimeFactorA = [0]*1000001
cache[1]=dict()
i=2
LeastPrimeFactorA[1]=1
while i<1000001:
    if LeastPrimeFactorA[i]==0:
        for j in xrange(i,1000001,i):
            LeastPrimeFactorA[j]=i
    i+=1
#print (LeastPrimeFactorA[:30])   

def primedecomp(n):
    if n==1:
        return dict()
    if n in cache:
        return cache[n]
    else:
        leastprimefactor = LeastPrimeFactorA[n]
        primed = primedecomp(n/leastprimefactor).copy()
        primed[leastprimefactor]=primed.get(leastprimefactor,0)+1
        cache[n]=primed
        return primed
def computeL(n):
    ans = 1
    if n%2==1:
        return 0
    if n%4==0:
        res = cache[n/4]
        for exponent in res.values():
            ans*=(exponent+1)
        return ans/2
    else:
        if n%2==0:
            return 0
        else:
            res = cache[n]
            for exponent in res.values():
                ans*=(exponent+1)
            return ans/2


for i in xrange(2,1000001):
    primedecomp(i)

#print computeL(1000000)
count = 0
for i in xrange(2,1000001):
    count +=computeL(i)
print count
print time.time()-start