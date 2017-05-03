import time
start = time.time()
count = {}
s = set()
two = set()
summ = 0
LIMIT = 10**12

for power in xrange(3,40):
    base = 2
    val = (base**power-1)/(base-1)
    if val>=LIMIT:
        break
    while val<LIMIT:
        two.add(val)
        base+=1
        val = (base**power-1)/(base-1)
    
print 'here',sum([1,7,13,15,21,31,40,43]),sum(two)+1
print sum(two)+1

print time.time()-start