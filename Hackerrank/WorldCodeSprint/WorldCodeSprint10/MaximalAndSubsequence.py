n,k = map(int,raw_input().split())
arr = []
for _ in xrange(n):
    arr.append(input())

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m


def ncr2(n,k):
    if k>n:
        return 0
    ans = 1
    for num in xrange(n-k+1,n+1):
        ans*=num
    #print 'ans',ans
    for num in xrange(1,k+1):
        ans*=modinv(num,1000000007)
    return ans
#print 'ncr',ncr2(5,2)%1000000007
def findMaxPower(arr):
    maxn = max(arr)
    i=0
    while(1<<i)<maxn:
        i+=1
    return i-1

#print 1<<findMaxPower([1,2,7])
#print 1<<findMaxPower([1,2,7,16])
#print 'a',arr
numberOfbits = findMaxPower(arr)
for bit in reversed(xrange(numberOfbits+1)):
    #print 1<<bit
    res = []
    for number in arr:
        if (1<<bit)&number:
            res.append(number)
    #print arr,res,len(res),k
    if len(res)>=k:
    #    print 'here',len(res),k
        arr = res
#print arr,n,k
print reduce(lambda x,y:x&y, arr)
print ncr2(len(arr),k)%1000000007
