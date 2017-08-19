def isAwin(s, t):
    ds = {}
    for l in s:
        ds[l] = ds.get(l, 0) + 1
    dt = {}
    for l in t:
        dt[l] = dt.get(l, 0) + 1
    isAwin = None
    for val in ds:
        if val not in dt:
            if ds[val] > 1:
                return True
    return False


def isBlose(s, t):
    ds = {}
    for l in s:
        ds[l] = ds.get(l, 0) + 1
    dt = {}
    for l in t:
        dt[l] = dt.get(l, 0) + 1
    ans = None
    for val in ds:
        if val not in dt:
            if ds[val] == 0:
                ans = True
    if ans:
        for val in dt:
            if val not in ds:
                return False
        return True
    return False


def solution(s, t):
    if isAwin(s, t):
        return "A"
    else:
        if isBlose(s, t):
            return "A"
    return "B"


T = input()
for _ in xrange(T):
    s = raw_input()
    t = raw_input()
    print solution(s, t)