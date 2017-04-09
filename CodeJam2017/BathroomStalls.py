import heapq
import time
def bathroomStall(n,k):
    res = []
    heapq.heappush(res,-n)
    for i in xrange(k-1):
        maxvalue = -heapq.heappop(res)
        heapq.heappush(res,-((maxvalue-1)/2))
        heapq.heappush(res,-(maxvalue-(maxvalue-1)/2-1))
    maxvalue = -heapq.heappop(res)
    return (maxvalue-1)/2,maxvalue-(maxvalue-1)/2-1

def bathroomStall2(n,k):
    import math
    maxvalue = math.ceil((n-k)/float(k+1))
    return (maxvalue-1)/2,maxvalue-(maxvalue-1)/2-1
#print bathroomStall(6,2)
start = time.time()
f = open('input.txt','r')
T = int(f.readline())#input()
for i in xrange(1,T+1):
    n,k = map(int, f.readline().split())
    res = bathroomStall(n,k)
    print "Case #%i: %i %i"%(i,max(res),min(res))
print time.time()-start
