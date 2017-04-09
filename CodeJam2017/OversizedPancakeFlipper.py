def flip(s):
    res = []
    for l in s:
        if l=='+':
            res.append('-')
        else:
            res.append('+')
    return "".join(res)

def countFlips(s,k):
    count = 0
    for i in xrange(len(s)-k+1):
        #print s
        if s[i]=='-':
            s = s[:i]+flip(s[i:i+k])+s[i+k:]
            count+=1
        
    if s.count('+')==len(s):
        return count
    else:
        return -1

#T = input()
#for i in xrange(1,T+1):
#    s,k = raw_input().split()
#    res = countFlips(s,int(k))
#    if res!=-1:
#        print "Case #%i: %i"%(i,res)
#    else:
#        print "Case #%i: %s"%(i,"IMPOSSIBLE")
