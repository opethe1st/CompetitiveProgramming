import sys
from math import pi

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
r = map(int, raw_input().strip().split(' '))
# Write Your Code Here
solutions = {}
def m(n,k):
    """ expected sum of r[:n] after k collisions"""
    return sum(r[:n])

def nm(n,k):
    """number of possible sums of r[:n]"""
    print 'n,m', n,k
    if k==0:
        return n
    elif k==1:
        return n-1
    else:
        return 0
    pass

def sol(n,k):
    print 'sol',n,k
    if solutions.get((n,k),False):
        return solutions[(n,k)]
    if (n-k-1)==0:
        #print 'ans',sum(r[:n])**2
        return sum(r[:n])**2
    if k==0:
        s=0
        for rad in r[:n]:
            s+=rad**2
        #print "ans k",s
        return s
    summ = 0.0
    a=( sol(n-1,k) + r[n-1]**2 )*float(n-1)/n
    print 'a',a
    b=(sol(n-1,k-1) + 2*sum(r[:n-1])*r[n-1] *r[n-1]**2)/float(n)
    print 'b',b,n-k,sum(r[:n-1]),r[n-1]
    solutions[(n,k)]=a+b
    return a+b
print "%.10f"%(pi*sol(n,k)) 