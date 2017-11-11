def countVillages(s):
    nControlledByA = 0
    nControlledByB = 0
    state = 'start'
    count = 0
    for i in range(len(s)):
        if s[i] == 'A':
            if state == 'A':
                # add all the empty villages between two A villages
                nControlledByA += count
            nControlledByA += 1
            state = 'A'
            count = 0
        elif s[i] == 'B':
            if state == 'B':
                # add all the empty villages between two B villages
                nControlledByB += count
            nControlledByB += 1
            state = 'B'
            count = 0
        elif s[i] == '.':
            if 0 < i < len(s)-1:
                if state == 'A':
                    count += 1
                elif state == 'B':
                    count += 1
        else:
            raise Exception('The only allowed characters are A, B and "." . Your input has {c}'.format(c='s[i]'))  # pylint: disable=E501
    return nControlledByA, nControlledByB

T = int(input())

for _ in range(T):
    s = input()
    a, b = countVillages(s)
    print('{A} {B}'.format(A=a, B=b))
