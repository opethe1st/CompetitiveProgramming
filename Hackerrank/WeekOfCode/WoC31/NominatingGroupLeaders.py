import sys


def count(v,l,r,x):
    d = {}
    for i in xrange(l,r+1):
        d[v[i]]+=d.get(v[i],0 )+1
    for id in v:
        if d[id]==x:
            return id
    else:
        return -1


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    v = map(int, raw_input().strip().split(' '))
    g = int(raw_input().strip())
    for a1 in xrange(g):
        l,r,x = raw_input().strip().split(' ')
        l,r,x = [int(l),int(r),int(x)]
        print count(v,l,r,x)