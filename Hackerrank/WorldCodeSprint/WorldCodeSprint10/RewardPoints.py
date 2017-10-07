month= map(int,raw_input().split())
print sum([100 if (month[i]>10) else month[i]*10  for i in xrange(3)]) 