
import itertools


n,k = map(int,raw_input().split())
w = [0 for i in xrange(n+1)]
d = [0 for i in xrange(n+1)]
for i in xrange(1,n+1):
    d[i],w[i]= map(int,raw_input().split())

for i,j,k in itertools.combinations(6,3):
    
