"""
Problem Description - https://code.google.com/codejam/contest/dashboard?c=6254486#s=p0
"""
def setDigit(n):
    if n==0:
        return "INSOMNIA"
    st = set()
    m=0
    p=0
    while(len(st)!=10):
        p += n
        m=p
        while m>0:
            st.add(m%10)
            m/=10  
    return p

#"""
T = input()
for i in xrange(1,T+1):
    N = input()
    res = setDigit(N)
    print "Case #%s: %s"%(i,str(res))
#"""