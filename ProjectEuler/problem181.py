cache = dict()
def combine(b,w):
    #print b,w
    if b==0 and w==0:
        return 0
    if (b+w)==1:
        return 1
    if (b+w)==2:
        return 2
    if (b,w) in cache:
        return cache[(b,w)]
    else:
        ans = 0
        for i in xrange(b+1):
            for j in xrange(w+1):
                #print i,j
                if not(i==0 and j==0):
                    print "here",i,j
                    ans+=combine(b-i,w-j)
        #ans+=combine(b,)
        cache[(b,w)]=ans
        return ans

print combine(5,0) 
print cache