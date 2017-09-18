from itertools import combinations

def canFormSquares(d1,d2):
    squares = set([i**2 for i in xrange(1,10)])
    combos = set()
    count=0
    for i in d1:
        for j in d2:
            combos.add(i*10+j)
            combos.add(j*10+i)
            if i==6:
                combos.add(j*10+9)
            if i==9:
                combos.add(j*10+6)
            if j==6:
                combos.add(i*10+9)
            if j==9:
                combos.add(i*10+6)
    #print d1,d2                
    #print squares
    #print combos
    return combos.issuperset(squares)

print canFormSquares((1, 4, 5, 6, 8, 9), (0, 2, 3, 4, 8, 9))
#"""
s = set()
count = 0
for dice1 in combinations(range(10),6):
    if 6 in dice1:
        dice1= list(dice1)
        dice1.append(9)
    elif 9 in dice1:
        dice1= list(dice1)
        dice1.append(6)
    for dice2 in combinations(range(10),6):
        if 6 in dice2:
            dice2= list(dice2)
            dice2.append(9)
        elif 9 in dice2:
            dice2= list(dice2)
            dice2.append(6)
        if canFormSquares(dice1,dice2):
            if dice1<dice2:
                count+=1
print count
#"""