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
            nm = a/b +int(a%b>0)
            nums[ti::i] = [0]*nm
        i = i+1
    for b in xrange(i,n):
        if nums[b] is 1:
            listofprimes.append(b)

    return listofprimes
count = 0
primes = primeslessthan(100000000)
#print len(primes)
for i in xrange(len(primes)):
    for j in xrange(i,len(primes)):
        if primes[i]*primes[j]<100000000:
            count+=1
        else:
            break
print count