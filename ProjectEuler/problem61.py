import bisect
from time import time
begin = time()

def leftBinarySearch(arr,val):
    return bisect.bisect_left(arr, val)
Figurates = []
Figurates.append([n*(n+1)/2 for n in xrange(0,300) if 1000<=(n*(n+1)/2)<=9999 ]) #Triangle numbers
Figurates.append([n**2 for n in xrange(0,201) if 1000<=(n**2)<=9999 ]) #Squrenumbers
Figurates.append([n*(3*n-1)/2 for n in xrange(0,201) if 1000<=(n*(3*n-1)/2)<=9999 ]) #pentagonal numbers
Figurates.append([n*(2*n-1) for n in xrange(0,201) if 1000<=(n*(2*n-1))<=9999 ]) #hexagonal numbers
Figurates.append([n*(5*n-3)/2 for n in xrange(0,201) if 1000<=n*((5*n-3)/2)<=9999 ]) #heptagonal numbers
Figurates.append([n*(3*n-2) for n in xrange(0,201) if 1000<=(n*(3*n+2))<=9999 ]) #octagonal numbers


def findCycle(start,end,allowedFigurates,n):
    #print bin(allowedFigurates),n,start,end
    if n==0:
        if start==end:
            return ['ans']
        else:
            return []
    for bit in xrange(5):
        if ((1<<bit) & allowedFigurates)!=0:
            #print bin(allowedFigurates),bin(1<<bit)
            index = leftBinarySearch(Figurates[bit],start*100)
            possibleAns = []
            while 0<=index<len(Figurates[bit]) and (Figurates[bit][index]/100)==start:
                num = Figurates[bit][index]
                ans = findCycle(num%100,end,allowedFigurates^(1<<bit),n-1)
                if ans!=[] or n==0:
                    ans = [num]+ans
                    #possibleAns.append(ans)
                    return ans
                index+=1
    return []

#print findCycle(10,8,(1<<6),6)
for num in Figurates[5]:
    #print num
    start = num/100
    end = num%100
    ans = findCycle(end,start,2**5-1,5)
    if ans:
        print sum([start*100+end]+ans[:-1])

end = time()
print end - begin