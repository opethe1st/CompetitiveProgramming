# Enter your code here. Read input from STDIN. Print output to STDOUT
#find those parts that are accessing or descending and modify appropriately
#find  a sequence is increasing the 
N = input()
A = []
for _ in xrange(N):
    A.append(input())

candie = [1]*N
increasing = True
decreasing = False
direction = True
for i in xrange(1,N):
    if A[i-1]<A[i]:
        if direction==increasing:
            candie[i]=candie[i-1]+1
        else:
            candie[i]=2
            direction = increasing
    else:
        if direction==decreasing:
            candie[i]=candie[i-1]+1
        else:
            candie[i]=1
            direction = decreasing
#print A
#print candie
print sum(candie)