from useful import primeslessthan,modinv

summ = 4 #for p = 5
primes = primeslessthan(10**8)[3:]
#print primes
#print modinv(2,7)
for p in primes:
    s = -1
    pfactorial = -1
    for i in xrange(1,5):
        pfactorial*=modinv(p-i,p)
        #print 'pfact',i,pfactorial,p-i,modinv(p-i,p)
        s+=pfactorial
    s = s%p
    #print p,s
    summ+=s

print summ