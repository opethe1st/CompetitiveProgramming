
OPEN = True
CLOSE = False
count = 0

def nextState(state,inp,i):
    global count
    if state==OPEN:
        if inp=='(' and count>=0:
            count+=1 #count the number of (
            validSeq[i]=1 #mark as (
            return OPEN
        elif inp==')' and count>0:
            count-=1
            validSeq[i]=-1
            return OPEN
        elif inp==')' and count==0:
            validSeq[i]=-1
            return CLOSE
    else:
        if inp=='(':
            count=1 #reset counter
            validSeq[i]=1
            return OPEN
        elif inp==')':
            validSeq[i]=-1
            return CLOSE


def bracketSequencePattern(brSeq):
    global validSeq
    global count
    lastopen = 0
    lastclose = 0
    count = 0
    validSeq = [10]*len(brSeq)
    state = OPEN
    n = len(brSeq)
    for i in xrange(n):
        print validSeq,count
        state = nextState(state,brSeq[i],i)
    print brSeq
    #print lastopen,lastclose,count
    return validSeq

c = bracketSequencePattern("(()))())(")
print 'c',bracketSequencePattern("(()))())(")