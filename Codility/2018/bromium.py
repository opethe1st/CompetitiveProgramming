from collections import defaultdict

def solution(N, Q, B, C):
    # write your code in Python 3.6
    countColourDict = defaultdict(dict)
    for k, bucket in enumerate(B):
        countColourDict[bucket][C[k]] = countColourDict[bucket].get(C[k], 0) + 1
        if countColourDict[bucket][C[k]] >= Q:
            return k
    return -1


print(solution(
    N=3,
    Q=2,
    B=[1, 2, 0, 1, 1, 0, 0, 1],
    C=[0, 3, 0, 2, 0, 3, 0, 0]
))
