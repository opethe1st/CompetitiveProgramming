
def solution(A):
    """This solution is in O(n) time and O(1) space. 
    We iterate through the value of p which defines the position at which the array is split into two nonempty arrays(left and right). 
    Initially p is 0 (this always valid since N>=2) - and we calculate this first before we are in the loop.
    and we save the absolute difference between the left array and the right array in minidiff.
    left stores the sum of items in the left array and right stores the sum of the items in the right array. 
    Whenever we increase the value of p left increases by A[p] and right decreases by A[i], we find abs(left-right) 
    and check if it is smaller than the smallest absolute difference of the sum of the left and right arrays so far - which is
    stored in minidiff. 
    if it is, we store abs(left-right) in minidiff. At the end of the loop, minidiff contains the lowest possible absolute 
    difference between left and right array and it is returned by the function  
    This solution is O(n) since the time it takes to loop is dominated by the loop which is proportional to the len of the 
    Array. It is O(1) space, since it uses just constant space no matter the array, left,right and minidiff (and perhaps p?)
    are its only storage requirements when it is run."""

    #p = 0
    left = A[0]
    right = sum(A) - A[0]
    minidiff = abs(left - right)

    for p in xrange(1, len(A) - 1):
        left += A[p]
        right -= A[p]
        print left, right, left + right
        if abs(left - right) < minidiff:
            minidiff = abs(left - right)
    return minidiff


print solution([1, 1])
