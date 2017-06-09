import sys
from math import pi

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
r = map(int, raw_input().strip().split(' '))
# Write Your Code Here
sumsq = sum([rad**2 for rad in r])
print sumsq
combos = (sum(r)**2 - sumsq)
print combos
def simulate(r,k):
    if (len(r)-k-1)==0:
        return sum(r)**2
    if k==0:
        s=0
        for rad in r:
            s+=rad**2
        return s
    #if k==2:
    #    sumsq = sum([rad**2 for rad in r])
    #    combos = (sum(r)**2 - sumsq)
    #    n = len(r)
    #    print 'n',n,(n*(n-1))/2
    #    return 2*(sumsq+ ( ((n-1)**2-1) *combos)/ (n*(n-1)*(n-1)*(n-2)/4.0) )
    s = 0.0
    for l in xrange(k):
        for i in xrange(len(r)):
            for j in xrange(len(r)-1):
                newr = r[:]
                a1=newr.pop(i)
                a2=newr.pop(j)
                newr.append(a1+a2)
                s+=simulate(newr,k-1)
    return s/(len(r)*(len(r)-1))
#looks like formula is k*(sumsq+(nc2+n-1c2-1)*combos)15 10 6 3 1 -1 2*(sumq+(8*combos)/18),sumsq+combos/10.0
print "%.10f"%(simulate(r,k)) ,2*(sumsq+(24*combos)/150.0),sumsq+(4*7*combos)/120.0