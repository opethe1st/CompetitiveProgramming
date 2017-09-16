B = 40
W = 60
N = (B+1)*(W+1)
dp = [0 for i in xrange(322)]
#dp[0] = 1
#dp[41] = 1
possibleCombos = []
for b in xrange((B+1)):
    for w in xrange(W+1):
        possibleCombos.append((w,b))

possibleCombos=possibleCombos[1:]
possibleCombos.sort()
#print possibleCombos

ndp = [[[[0 for k in xrange(61)] for i in xrange(61)] for j in xrange(61)] for l in xrange(61)]
ndp[0][0][B][W]=1
for b in xrange(61):
    for w in xrange(41):
        for lb in xrange(b+1):
            for lw in xrange(w+1):
                ndp[b][w][lb][lw]+=ndp[b+lb][w-lw][lb-1][lw-1]
print ndp[60][40][0][0]
cache = {}
cache[(0,0)]=1
def count(possibleCombos,wb,leastcombo,c):
    print wb,c
    if wb[0]<0 or wb[1]<0:
        #print 0   
        return 0
    if (wb,leastcombo) in cache:
        return cache[(wb,leastcombo)]
    if wb ==(0,0):
        return 1
    else:
        ans=0
        for combo in possibleCombos:
            
            if combo>=leastcombo and wb[0]-combo[0]>=0 and wb[1]-combo[1]>=0:
                ans+=count(possibleCombos,(wb[0]-combo[0],wb[1]-combo[1]), combo,c+1)
        cache[(wb,leastcombo)]=ans
        #print 'ans',ans
        return ans
#Ans : 83735848679360680
#print count(possibleCombos,(W,B),(0,0),0)
