import time
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    #s is now 0
    if t==0: #at the same spot
        return 0
    if t>s:
        t = t-s
    else:
        t=n+s-t
    
    myR=R[s:]+R[:s] #rotate R and make s=0
    if myR[0]==0: #cannot move from s
        return -1

    maxPositionFF = [0]*n #max forward position forward
    maxPositionFF[0]=myR[0] #starting from s
    for i in xrange(1,n):
        maxPositionFF[i]=max( myR[i] + i,maxPositionFF[i-1] )
    
    maxPositionFB = [0]*n #max forward position backward. Forward direction but backwards
    maxPositionFB[0]=myR[0] #starting from s
    for i in xrange(1,n):
        maxPositionFB[n-i] = max(((-i) + myR[n-i]) , maxPositionFB[(n-i+1)%n] )

    maxPositionBF = [0]*n #max backward position forward
    maxPositionBF[0]=-myR[0] #starting from s
    for i in xrange(1,n):
        maxPositionBF[i]=min(i-myR[i] , maxPositionBF[i-1])
    for i in xrange(n):
        maxPositionBF[i]= -maxPositionBF[i]
    
    maxPositionBB = [0]*n #starting from s too
    maxPositionBB[0] = (n-myR[0])
    for i in xrange(1,n):
        maxPositionBB[n-i] = min((n-i)-myR[n-i] , maxPositionBB[(n-i+1)%n] )
    #debug
    print myR
    print maxPositionFF
    print maxPositionFB
    print maxPositionBF
    print maxPositionBB

    time = 0
    fpos = maxPositionFF[0]
    bpos = maxPositionBB[0]
    while time<n:
        time+=1
        if fpos>=t:
            mintime=time
            break
        if bpos<=t-n:
            mintime=time
            break

        nfpos = max(maxPositionFF[fpos],maxPositionBF[bpos])
        nbpos = min(maxPositionBB[fpos],maxPositionFB[bpos])
        fpos=nfpos
        bpos=nbpos
    
    if mintime!=float('inf'):
        return mintime
    else:
        return -1



start = time.time()

n, s, t = 10,0,5#raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = 1, 3, 4, 7#raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]

visited=[False]*n
R = [0]*n 
R[0]=r_0
for i in range(1,n):
    R[i]=(R[i-1]*g+seed)%p

#print R

result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
print time.time()-start