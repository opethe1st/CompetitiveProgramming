
#Peter
peter = [0]*37
for a in xrange(1,5):
    for b in xrange(1,5):
        for c in xrange(1,5):
            for d in xrange(1,5):
                for e in xrange(1,5):
                    for f in xrange(1,5):
                        for g in xrange(1,5):
                            for h in xrange(1,5):
                                for i in xrange(1,5):
                                    peter[a+b+c+d+e+f+g+h+i]+=1

collins = [0]*37
for a in xrange(1,7):
    for b in xrange(1,7):
        for c in xrange(1,7):
            for d in xrange(1,7):
                for e in xrange(1,7):
                    for f in xrange(1,7):
                        collins[a+b+c+d+e+f]+=1
#print sum(peter), sum(collins)
scollins = float(sum(collins))
speter = float(sum(peter))
for i in xrange(len(peter)):
    peter[i] = peter[i]/speter
for i in xrange(len(collins)):
    collins[i] = collins[i]/scollins

prefixsumCollins = [0]*38
for i in xrange(1,38):
    prefixsumCollins[i]=prefixsumCollins[i-1]+collins[i-1]
#print collins,sum(collins)
#print prefixsumCollins[37]
ans = 0
for i in xrange(len(peter)):
    ans+=peter[i]*prefixsumCollins[i]
print "%.7f"%ans
