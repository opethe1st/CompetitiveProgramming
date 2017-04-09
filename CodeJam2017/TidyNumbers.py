
def lastTidyNumber(n):
    s = str(n)
    prev = 0
    ans = ""
    last = 0
    for i in xrange(len(s)):
        if prev<int(s[i]):
            last = i
        if prev>int(s[i]):
            j = last
            ans = s[:j]+str(int(s[j])-1)+"9"*(len(s)-j-1)
            break
        prev = int(s[i])
    else:
        return n
    return long(ans)

#print lastTidyNumber("12310")
#print lastTidyNumber("600")

T = input()
for i in xrange(1,T+1):
    s = input()
    res = lastTidyNumber(s)
    print "Case #%i: %d"%(i,res)
    
