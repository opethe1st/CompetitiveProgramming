def getMinMoves(arr):
    if sum(arr) % len(arr) != 0:
        return -1
    else:
        goal = sum(arr)/len(arr)
        ans = 0
        for i in xrange(len(arr)-1):
            diff = goal - arr[i]
            ans += abs(diff)
            arr[i] += diff
            arr[i+1] -= diff
        return ans


def minimumMovesEqual(arr, d):
    # calculate the minimum number of moves to get all elements equal
    D = [[] for i in xrange(d)]
    for i in xrange(len(arr)):
        D[i % d].append(arr[i])
    ans = 0
    for subarr in D:
        res = getMinMoves(subarr)
        if res == -1:
            return -1
        ans += res
    return ans

T = input()
for _ in xrange(T):
    n, d = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    print minimumMovesEqual(arr, d)
