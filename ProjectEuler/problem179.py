import time
start = time.time()
cache = dict()
LeastPrimeFactorA = [0]*10000001
cache[1]=dict()
nFactors = dict()
nFactors[1]=1
i=2
LeastPrimeFactorA[1]=1
while i<10000001:
    if LeastPrimeFactorA[i]==0:
        for j in xrange(i,10000001,i):
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
def numberOfFactors(n):
    if n in nFactors:
        return nFactors[n]
    res = cache[n]
    ans=1
    for exponent in res.values():
        ans*=(exponent+1)
    nFactors[n]=ans
    return ans
    


for i in xrange(2,10000001):
    primedecomp(i)

#print computeL(1000000)
count = 0
for n in xrange(2,10000001):
    
    count +=int(numberOfFactors(n)==numberOfFactors(n-1))
print count
print time.time()-start