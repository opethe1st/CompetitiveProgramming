"Problem Description - https://code.google.com/codejam/contest/dashboard?c=6254486#s=p1"
def count(a):
    if len(a)==1 and a[0]=='+':
        return 0
    elif len(a)==1 and a[0]=='-':
        return 1
    count=0
    prev = a[0]
    for i in xrange(1,len(a)):
        if prev!=a[i]:
            count+=1
        prev=a[i]
    #print a,count
    if a[-1]=='+':
        return count
    else:
        return count+1

T = input()
for i in xrange(1,T+1):
    a = raw_input()
    res = count(a)
    print "Case #%s: %s"%(i,str(res))
