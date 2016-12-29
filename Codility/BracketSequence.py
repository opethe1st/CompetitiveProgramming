"Codility Titantium."

#count = 0

OpenState = True
CloseState = False
Valid = 2

#lastopen=0
#lastclose=0

def findLastOpen(validSeq,pos,lastopen,lastclose):
    while pos>lastclose and validSeq[pos]!=1:
        pos-=1
    if validSeq[pos]==1:
        return pos
    else:
        return -1 #indicate not found

def nextState(state,inp,i,lastopen,lastclose,count):
    #global lastopen
    #global lastclose
    #global count
    if state==OpenState:
        if inp=='(' and count>=0:
            count+=1
            validSeq[i]=1
            lastopen=i
            return OpenState
        elif inp==')' and count>=0:
            count-=1
            l= findLastOpen(validSeq,i,lastopen,lastclose)
            if l==-1:
                validSeq[i]=-1
                return CloseState
            else:
                validSeq[i]=0
                validSeq[l]=0
            
            return OpenState
        elif inp==')' and count==0:
            count-=1
            validSeq[i]=0
            validSeq[lastopen]=0
            lastopen=0
            return CloseState
    else:
        if inp=="(":
            validSeq[i]=1
            count=1
            lastopen=i
            return OpenState
        elif inp==")":
            validSeq[i]=-1
            count-=1
            lastclose=i
            return CloseState


def bracketSequencePattern(brSeq):
    global validSeq
    lastopen = 0
    lastclose = 0
    count = 0
    validSeq = [10]*len(brSeq)
    state = CloseState
    n = len(brSeq)
    for i in xrange(n):
        #print validSeq,count
        state = nextState(state,brSeq[i],i,lastopen,lastclose,count)
    #print brSeq
    #print lastopen,lastclose,count
    return validSeq

#bracketSequencePattern([')(()'])
#bracketSequencePattern(")()()(")
#bracketSequencePattern(")))(((")
#bracketSequencePattern("()")
#bracketSequencePattern(")(")
#a = bracketSequencePattern(")))))()((())(((())))")
#b = bracketSequencePattern(")))((()))")
#c = bracketSequencePattern("(()))())(")
#print 'c',bracketSequencePattern("(()))())(")
#print a
def findLongestValid(seQ):
    #find the indices with zero.
    prev = -1
    limits =[]
    for i in xrange(len(seQ)):
        if seQ[i]==0 and prev!=0:
            start=i
            prev = 0
        elif seQ[i]==0 and prev==0:
            end = i
            prev = 0
        elif (seQ[i]!=0 and prev==0):
            limits.append((start,end))
            prev = seQ[i]
        elif prev!=0:
            prev=seQ[i]
    if prev==0:
        limits.append((start,end))
        prev = seQ[i]
    return limits 
#print findLongestValid(a)

def rotateOnce(seQ):
    """returns the length of the current largest valid"""
    print 'seQ',seQ
    l = findLongestValid(seQ)
    #print l
    mx =0
    maxSeq = ()
    for zeroSeq in l:
        if mx<zeroSeq[1]-zeroSeq[0]+1:
            mx = zeroSeq[1]-zeroSeq[0]+1
            maxSeq = zeroSeq
    #return maxSeq
    if seQ[maxSeq[0]-1]==seQ[maxSeq[0]-2] and maxSeq[0]>1 and len(l)>0:
        seQ[maxSeq[0]-1]=0
        seQ[maxSeq[0]-2]=0
    l = findLongestValid(seQ)
    #print l
    return seQ

def lengthLongestValid(seQ):
    l = findLongestValid(seQ)
    #print l
    mx =0
    maxSeq = ()
    for zeroSeq in l:
        if mx<zeroSeq[1]-zeroSeq[0]+1:
            mx = zeroSeq[1]-zeroSeq[0]+1
            maxSeq = zeroSeq
    return mx
#print rotateOnce(b)
#print lengthLongestValid(c)

class Solution(object):
    def longestValidParentheses(self,s):
        seQ = bracketSequencePattern(s)
        l = findLongestValid(seQ)
        #print l
        mx =0
        maxSeq = ()
        for zeroSeq in l:
            if mx<zeroSeq[1]-zeroSeq[0]+1:
                mx = zeroSeq[1]-zeroSeq[0]+1
                maxSeq = zeroSeq
        return mx

soln = Solution()
print soln.longestValidParentheses("(()))())(")