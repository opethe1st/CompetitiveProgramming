def isSorted(arr):
    "check if sorted in ascending order"
    for i in xrange(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    else:
        return True

def accurateSorting(arr):
    for i in xrange(1,len(arr)):
        if arr[i-1]==(arr[i]+1):
            #swap the two values
            temp = arr[i-1]
            arr[i-1]=arr[i]
            arr[i]=temp
    if isSorted(arr):
        return True
    else:
        return False

#tests
print accurateSorting([1,0,3,2])
print accurateSorting([2,1,0])