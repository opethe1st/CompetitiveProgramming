primes = set([2,3,5,7,11,13,17,19,23,29,31,37,41])
def cond(a):
    a,b,c,d,e = a
    if a+b+c+d+e in primes and a+b+c+d in primes and b+c+d+e in primes and a+b+c in primes and b+c+d in primes and c+d+e in primes: 
        return True
    else:
        return False
s = 0
for a in xrange(1,10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                for e in xrange(10):
                    for f in xrange(10):
                        for g in xrange(10):
                            for h in xrange(10):
                                for i in xrange(10):
                                    for j in xrange(10):
                                        if cond([a,b,c,d,e]) and cond([b,c,d,e,f]) and cond([c,d,e,f,g]) and cond([d,e,f,g,h]) and cond([e,f,g,h,i])  and cond([f,g,h,i,j]):
                                            s+=1
                                        #print a,b,c,d,e,f,g,h
#f(7) is 101
#f(6) is 95
#f(5) is 218
#f(8) is 295
#f(9) is 513
print s