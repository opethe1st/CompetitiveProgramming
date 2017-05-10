import time 
start = time.time()

limit = 1000000
leastPrimeFactor = [0]*limit
leastPrimeFactor[1]=1
i = 2
while i<limit:
    if leastPrimeFactor[i]==0:
        for j in xrange(i,limit,i):
            leastPrimeFactor[j]=i
    i+=1

def primedecomp(n):
    pf = {}
    while leastPrimeFactor[n]!=1:
        pf[leastPrimeFactor[n]] = pf.get(leastPrimeFactor[n],0)+1
        n/=leastPrimeFactor[n]
    return pf

def sumdivisors(n):
    pf = primedecomp(n) #primefactorisation
    if len(pf)==0:
        return 1
    return reduce(lambda x,y:x*y, [(p**(pf[p]+1)-1)/(p-1) for p in pf])-n

def chain(n):
    if n in computedchain:
        return computedchain[n]
    m = sumdivisors(n)
    
    count = 0
    s = set()
    while m not in s:
        #print m
        s.add(m)
        if m>1000000:
            return 0
        m=sumdivisors(m)
        count+=1
    #print 'min s',min(s)
    if n in s:
        computedchain[n]=len(s)
        return len(s)
    else:
        return 0
    return count
#print chain(220)
computedchain={}
#print sumdivisors(562)
print chain(14316)
#"""
maxi =0
maxval=1
for i in xrange(2,limit):
    #print i
    lengthChain = chain(i)
    if lengthChain>maxi:
        maxi=lengthChain
        maxval=i  
print maxi,maxval

print time.time()-start
#"""