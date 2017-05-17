
nWaysDic ={}
def nWays(n,tile,tileUsed):
    #print n,tile,tileUsed
    if n*100+tile*10+tileUsed in nWaysDic:
        return nWaysDic[n*100+tile*10+tileUsed]
    if not tileUsed:
        if n<tile:
            return 0
        elif n==tile:
            return 1
        elif n>tile:
            nWaysDic[n*100+tile*10+tileUsed] = nWays(n-tile,tile,not(tileUsed))+nWays(n-1,tile,tileUsed)
            return nWaysDic[n*100+tile*10+tileUsed]
    else:
        if n<tile:
            return 1
        elif n==tile:
            return 2
        else:
            nWaysDic[n*100+tile*10+tileUsed] = nWays(n-tile,tile,tileUsed)+nWays(n-1,tile,tileUsed)
            return nWaysDic[n*100+tile*10+tileUsed]


print nWays(50,4,False)+nWays(50,3,False)+nWays(50,2,False)
#print nWaysDic
#There is a faster way without using tileUsed
