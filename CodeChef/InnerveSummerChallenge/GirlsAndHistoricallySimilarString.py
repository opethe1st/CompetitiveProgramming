T = input()
for _ in xrange(T):
    a, b = raw_input().split()
    da = {}
    db = {}
    for l in a:
        da[l] = da.get(l, 0)+1
    for l in b:
        db[l] = db.get(l, 0)+1
    occurrenceA = []
    occurrenceB = []
    for val in da:
        occurrenceA.append(da[val])
    for val in db:
        occurrenceB.append(db[val])
    occurrenceA.sort()
    occurrenceB.sort()
    if occurrenceA == occurrenceB:
        print "YES"
    else:
        print "NO"
