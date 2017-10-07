
import sys
from math import ceil

def getMaxMonsters(n, hit, t, h):
    # Complete this function
    h.sort()
    nkilled = 0
    breakloop=False
    for mon in h:
        hitsRequiredToKill = int(ceil(mon/float(hit)))
        if t>=hitsRequiredToKill:
            t-=hitsRequiredToKill
            nkilled+=1
        else:
            return nkilled

    return nkilled

n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
result = getMaxMonsters(n, hit, t, h)
print(result)