import time
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
    #s is now 0
    for i in xrange(1,n):
        a = i-R[(s+i)%n]
        maxJBF[i]=min(i-R[(s+i)%n], maxJBF[i-1])

    if s<=t:
        #print 'here',s,t
        time = 0
        maxfd=0
        maxbd =0
        while True:
            #print maxfd,maxbd
            if maxfd>= t-s:
                return time
            if maxbd<= -(n-(t-s)):
                return time
            nmaxfd = max(maxJFF[maxfd%n], maxJFB[-maxbd%n])
            nmaxbd = min(maxJBB[-maxbd%n], maxJBF[maxbd%n])
            time+=1
            if nmaxfd==maxfd and nmaxbd==maxbd:
                return -1
            else:
                maxfd=nmaxfd
                maxbd=nmaxbd
    if s>=t:
        time = 0
        maxfd=0
        maxbd =0
        while True:
            if maxfd>=n-s+t:
                return time
            if maxbd<= s-t:
                return time
            nmaxfd = max(maxJFF[maxfd%n], maxJFB[-maxbd%n])
            nmaxbd = max(maxJBB[-maxbd%n], maxJBF[maxbd%n])

            if nmaxfd==maxfd and nmaxbd==maxbd:
                return -1
            else:
                nmaxfd=maxfd
                nmaxbd=maxbd
    


start = time.time()

n, s, t = 10000000,0,5000000#raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = 1, 3, 4, 7#raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]



visited=[False]*n
R = [0]*n 
R[0]=r_0
for i in range(1,n):
    R[i]=(R[i-1]*g+seed)%p

#print R
maxJFF = [0]*n
maxJFF[0]=R[0]
for i in xrange(1,n):
    a = i+R[s+i]
    maxJFF[i]=max(i+R[s+i], maxJFF[i-1])

maxJBB = [0]*n
maxJBB[0]= -R[0]
for i in xrange(1,n):
    a = -i-R[(s-i)%n]
    maxJBB[i]=min(-i-R[(s-i)%n], maxJBB[i-1])

maxJFB = [0]*n
maxJFB[0]=R[0]
for i in xrange(1,n):
    a = -i+R[(s-i)%n]
    maxJFB[i]=max(-i+R[(s-i)%n], maxJFB[i-1])

maxJBF = [0]*n
maxJBF[0]= -R[0]
print time.time()-start





result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
print time.time()-start