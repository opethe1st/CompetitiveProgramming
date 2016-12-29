"""
Week of Code 25 - https://www.hackerrank.com/contests/w25/challenges/append-and-delete/
"""
def numCommon(s,t):
    count = 0
    while count<min(len(s),len(t)) and s[count]==t[count]:
        count+=1
    return count

s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())

common = numCommon(s,t)
nLeftS =  len(s)-common
nLeftT = len(t)- common
#print nLeftS,nLeftT

if (k>(len(s)+len(t))):
    print "Yes"
elif (k>=(nLeftS+nLeftT) and (k-nLeftS-nLeftT)%2==0):
    print "Yes"
else:
    print "No"


