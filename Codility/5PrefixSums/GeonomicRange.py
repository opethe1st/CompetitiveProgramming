def solution(S, P, Q):
    # write your code in Python 2.7
    prefixA = [0] * (len(S) + 1)
    prefixC = [0] * (len(S) + 1)
    prefixG = [0] * (len(S) + 1)
    prefixT = [0] * (len(S) + 1)
    for i in xrange(len(S)):
        if S[i] == 'A':
            prefixA[i + 1] = prefixA[i] + 1
        else:
            prefixA[i + 1] = prefixA[i]
    for i in xrange(len(S)):
        if S[i] == 'C':
            prefixC[i + 1] = prefixC[i] + 1
        else:
            prefixC[i + 1] = prefixC[i]
    for i in xrange(len(S)):
        if S[i] == 'G':
            prefixG[i + 1] = prefixG[i] + 1
        else:
            prefixG[i + 1] = prefixG[i]
    for i in xrange(len(S)):
        if S[i] == 'T':
            prefixT[i + 1] = prefixT[i] + 1
        else:
            prefixT[i + 1] = prefixT[i]

    ans = []
    for i in xrange(len(P)):
        # print prefixC,Q[i],P[i]
        if prefixA[Q[i] + 1] > prefixA[P[i]]:
            ans.append(1)
        elif prefixC[Q[i] + 1] > prefixC[P[i]]:
            ans.append(2)
        elif prefixG[Q[i] + 1] > prefixG[P[i]]:
            ans.append(3)
        elif prefixT[Q[i] + 1] > prefixT[P[i]]:
            ans.append(4)
    return ans
