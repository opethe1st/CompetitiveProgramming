T = input()
for n in xrange(T):
    D,N = map(int,raw_input().split())
    K = []
    S = []
    for i in xrange(N):
        k,s = map(int,raw_input().split())
        K.append(k)
        S.append(s)
    #print K,S
    maxitime=0
    for i in xrange(N):
        t = (D-K[i])/float(S[i])
        maxitime = max(maxitime,t)
    print "Case #%i: %.6f"%(n+1,D/maxitime)