def canLetterBeFormed(NDict, letter):
    letter = str(letter)
    charDict = {}
    for l in letter:
        charDict[l] = charDict.get(l, 0)+1
    for l in charDict:
        if charDict[l] > NDict.get(l, 0):
            return False
    return True


def solution(N):
    N = str(N)
    NDict = {}
    for n in N:
        NDict[n] = NDict.get(n, 0)+1
    A = 65
    Z = 90
    ans = ''
    for letter in range(A, Z+1):
        if canLetterBeFormed(NDict, letter):
            ans += chr(letter)
    return ans
T = input()

for _ in xrange(T):
    N = input()
    print(solution(N))
