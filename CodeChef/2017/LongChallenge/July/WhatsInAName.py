def formatName(s):
    s = s.lower()
    names = s.split()
    fName = ""
    for i in range(len(names) - 1):
        fName += names[i][0].upper()+'. '
    fName += names[-1][0].upper()+names[-1][1:]
    return fName

T = input()
for _ in xrange(T):
    print formatName(raw_input())