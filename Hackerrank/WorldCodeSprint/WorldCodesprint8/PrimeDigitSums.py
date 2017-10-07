#World Code sprint

primes = set([2,3,5,7,11,13,17,19,23,29,31,37,41])

def cond(a):
    a,b,c,d,e = a
    if a+b+c+d+e in primes and a+b+c+d in primes and b+c+d+e in primes and a+b+c in primes and b+c+d in primes and c+d+e in primes: 
        return True
    else:
        return False

def chloelist():
    s = set()
    #s = []
    for a in xrange(10):
        for b in xrange(10):
            for c in xrange(10):
                for d in xrange(10):
                    for e in xrange(10):
                        if cond([a,b,c,d,e]):
                            s.add((a,b,c,d,e))
                            #s.append((a,b,c,d,e))
    return s

clist =chloelist() 
#print clist,len(clist)

ans = [0]*1001

dp = [[[[[0 for i in xrange(10)] for j in xrange(10)] for k in xrange(10)] for l in xrange(10)] for m in xrange(10)]
newdp =[[[[[0 for i in xrange(10)] for j in xrange(10)] for k in xrange(10)] for l in xrange(10)] for m in xrange(10)]
#mdp = [[[[[[0 for i in xrange(10)] for j in xrange(10)] for k in xrange(10)] for l in xrange(10)] for m in xrange(10)] for n in xrange(120)]

s1,s2,s3,s4,s5 = 0,0,0,0,0
for a in xrange(10):
    for b in xrange(10):
        for c in xrange(10):
            for d in xrange(10):
                for e in xrange(10):
                    if a==0 and b==0 and c>0 and (c+d+e) in primes:
                            #print a,b,c,d,e
                            s3+=1
                    if a==0 and b==0 and c==0 and d>0 and d+e in primes:
                            print a,b,c,d,e
                            s2+=1
                    if a==0 and b==0 and c==0 and d==0 and e in primes:
                            s1+=1
                    if (a+b+c+d+e) in primes and (b+c+d+e) in primes and (c+d+e) in primes and (a+b+c+d) in primes and (a+b+c) in primes and (b+c+d) in primes:
                        if a>0:
                            dp[a][b][c][d][e]=1
                            s5+=1
                        elif b>0:
                            s4+=1
                        elif c>0:
                            #print a,b,c,d,e
                            s3+=1
                        elif d>0:
                            s2+=1
                        elif e>0:
                            
                            s1+=1

ans[1]=s1
ans[2]=s2
ans[3]=s3
ans[4]=s4       
ans[5]=s5  
for i in xrange(5,1000+1):
    s = 0
    for a,b,c,d,e in clist:
        for f in xrange(10):
            if (b,c,d,e,f) in clist:
                newdp[b][c][d][e][f]+=dp[a][b][c][d][e]
                s+=dp[a][b][c][d][e]
    ans[i]=s
    dp = newdp 

print ans[:15]