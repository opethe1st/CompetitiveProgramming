import time
from math import sqrt
start = time.time()
limit = 64000000
leastPrimeFactor = [0]*limit
leastPrimeFactor[1]=1
i = 2
while i<limit:
    if leastPrimeFactor[i]==0:
        for j in xrange(i,limit,i):
            leastPrimeFactor[j]=i
    i+=1
#print leastPrimeFactor[:100]
def primedecomp(n):
    pf = {}
    while leastPrimeFactor[n]!=1:
        pf[leastPrimeFactor[n]] = pf.get(leastPrimeFactor[n],0)+1
        n/=leastPrimeFactor[n]
    return pf
def sigma2(n):
    pf = primedecomp(n) #primefactorisation
    if len(pf)==0:
        return 1
    return reduce(lambda x,y:x*y, [(p**(2*pf[p]+2)-1)/(p**2-1) for p in pf  ])

def isSquare(n):
    if n==(int(sqrt(n)))**2 or n==(int(sqrt(n))+1)**2:
        return True
    else:
        return False

#print isSquare(25)
#print isSquare(84100),primedecomp(246)
summ = 0
for i in range(1,limit):
    s = sigma2(i)
    if isSquare(s):
        #print i,s
        summ+=i
print summ
print time.time()-start