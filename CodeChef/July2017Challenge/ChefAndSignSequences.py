def minimumPossible(seq):
    p = 1
    positivep = 1
    negativep = 1
    for l in seq:
        if l == '<':
            negativep = 1
            positivep += 1
            p = max(positivep, p)
        elif l == '=':
            continue
        elif l == '>':
            positivep = 1
            negativep += 1
            p = max(negativep, p)
    return p

T = input()
for _ in xrange(T):
    print minimumPossible(raw_input())