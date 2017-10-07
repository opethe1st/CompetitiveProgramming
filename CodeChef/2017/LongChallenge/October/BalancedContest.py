def isCakeWalk(n, p):
    if n >= p//2:
        return True
    else:
        return False


def isHard(n, p):
    if n <= p//10:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    N, P = map(int, input().split())
    ncakewalkproblems = 0
    nhardproblems = 0
    for i in map(int, input().split()):
        if isCakeWalk(i, P):
            ncakewalkproblems += 1
        elif isHard(i, P):
            nhardproblems += 1
    if nhardproblems == 2 and ncakewalkproblems == 1:
        print('yes')
    else:
        print('no')
