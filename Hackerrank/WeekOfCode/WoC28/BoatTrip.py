#Question here - https://www.hackerrank.com/contests/w28/challenges/boat-trip/

n,c,m = raw_input().strip().split(' ')
n,c,m = [int(n),int(c),int(m)]
p = map(int, raw_input().strip().split(' '))
if max(p)<=m*c:
    print "Yes"
else:
    print "No"