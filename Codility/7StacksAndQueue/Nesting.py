def solution(S):
    count = 0
    for l in S:
        if l == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                return 0
    if count == 0:
        return 1
    else:
        return 0
