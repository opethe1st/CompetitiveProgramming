from functools import reduce

def xorsum(arr):
    return reduce(lambda x,y:x^y,arr)

#print xorsum([1,2,3,4])
count = 0
n = 1<<30
for i in xrange(1,n+1):
    if xorsum([i,2*i,3*i])==0:
        count +=1
print count