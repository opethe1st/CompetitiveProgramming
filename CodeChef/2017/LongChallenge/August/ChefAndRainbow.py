

def nextNum(i, direction):
    if 0 < i < 7 and direction:
        return i + 1
    elif 0 < i < 7 and not(direction):
        return i - 1
    elif i == 7:
        return 6
    else:
        return 1


def isRainbow(arr):
    ans = True
    #
    s17 = set([1, 2, 3, 4, 5, 6, 7])
    if not(s17.issubset(set(arr))):
        return False
    # test that it is oscilatting from 1 to 7 to 1.
    currentNum = 1
    direction = True
    for i in arr:
        if i == currentNum or i == nextNum(currentNum, direction):
            if i == 7:
                direction = False
                currentNum = i
            if i == nextNum(currentNum, direction):
                currentNum = i 
                #print currentNum,
        else:
            ans = False
            break

    # test if it's symmetric
    ans = ans and (arr == arr[::-1])
    return ans

#"""
T = input()
for _ in xrange(T):
    n = input()
    arr = map(int, raw_input().split())
    if isRainbow(arr):
        print "yes"
    else:
        print "no"
#"""


