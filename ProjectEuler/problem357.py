from math import sqrt
import math
import time
start = time.time()

N = 100000000
def primeslessthan(n):
    if n==1:
        return []

    nums =[1]*n
    listofprimes = []
    nums[0] =nums[1]=0
    i=2
    while i*i<n:
        if nums[i] is 1:
            listofprimes.append(i)
            ti = i*i
            a = n - ti
            b = i
            nm = int(a/b +int(a%b>0))
            nums[ti::i] = [0]*nm
        i = i+1
    for b in range(i,n):
        if nums[b] is 1:
            listofprimes.append(b)

    return listofprimes
#print primeslessthan(97)
primeslessthan108 = set(primeslessthan(N+1))
candidates = list(filter(lambda p: (((p-1)/2+2) in primeslessthan108),primeslessthan108  ))
#candidates = [num-1 for num in candidates]
print candidates[:10]
def isprimegen(n):
    for i in range(2,int(sqrt(n))):
        if n%i==0 and (i+(n/i)) not in primeslessthan108:
                return False
    return True

print (sum(list(filter(isprimegen,candidates))))

print (time.time()-start)
#print len(squarefreeNumbers(N))