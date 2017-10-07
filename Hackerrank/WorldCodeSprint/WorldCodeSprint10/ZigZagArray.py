n = input()
arr = map(int,raw_input().split())
count = 0
prevdirection = arr[0]<arr[1]
for i in xrange(1,n):
    direction = arr[i-1]>arr[i]
    if prevdirection==direction:
        count+=1
    prevdirection = direction
print count