
def solution(A):
    intersectPointsLeft = [(i-A[i], 0) for i in xrange(len(A))]
    intersectPointsRight = [(A[i]+i, 1) for i in xrange(len(A))]
    intersectPoints = intersectPointsLeft+intersectPointsRight
    intersectPoints.sort()
    count = 0
    ans = 0
    maxcount = 0
    # print intersectPoints
    for point in intersectPoints:
        if point[1] == 0:
            ans += count
            count += 1
        else:
            count -= 1
        maxcount = ma(maxcount, count)
    return ans

print solution([1, 5, 2, 1, 4, 0])