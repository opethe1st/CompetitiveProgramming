import time
start = time.time()
cache={}
st = set()
N = 20
#194505988824000
#199174132555776000
#selection*10+a[num]%10
a= range(N)
def doublePandigital(n,chosen,s):
    #print n,bin(chosen),s 
    if n==0:
        if s%11==0:
            return 1
        else:
            return 0
    if chosen*N**2+N*n+s in cache:
        return cache[chosen*N**2+N*n+s]
    res=0
    for num in xrange(N):
        if n==20 and a[num]%10==0:
            continue
        if (1<<num)&chosen:
            if n%2==0:
                res+=doublePandigital(n-1,chosen^(1<<num),(s-a[num]%10)%11)
            else:
                res+=doublePandigital(n-1,chosen^(1<<num),(s+a[num]%10)%11)
    cache[chosen*N**2+N*n+s]=res
    #print n,chosen,s
    return res

print doublePandigital(20,(1<<N)-1,0)/(2**10)
print time.time()-start