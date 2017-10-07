# Enter your code here. Read input from STDIN. Print output to STDOUT
#Week of Code 25 - https://www.hackerrank.com/contests/w25/challenges/baby-step-giant-step/copy-from/7613913
q = input()
for _ in xrange(q):
    a,b,d = map(int,raw_input().split())
    count = 0
    count = (d - 2*b)/b+1 if d>2*b else 0
    left = d-count*b
    if left==b or left==a:
        print count+1
    elif b<left<2*b:
        print count+2
    elif 0<left<b:
        print count+2
    elif left==0:
        print count