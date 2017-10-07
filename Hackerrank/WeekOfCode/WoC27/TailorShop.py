# Week of Code.. day 2 - https://www.hackerrank.com/contests/w27/challenges/tailor-shop/copy-from/8207732

import sys
import math

#Input
nclusters,price = raw_input().strip().split(' ')
nclusters,price = [int(nclusters),int(price)]
minCostForEachCluster = map(int,raw_input().strip().split(' '))

#Solution
#The idea behind the solution is to make sure we buy the least valid number of buttons that can be bought of
#any colour. the number has to be distinct (different from other numbers) and also has to be more than or equal 
#to the minimum number that must be bought

#minbuttons has the values of the minimum number of buttons that need to be bought.
minbuttons = [int(math.ceil(cost/float(price))) for cost in minCostForEachCluster]
minbuttons.sort()

#s = sum of buttons that need to be bought
s = 0
#buy the first button
s+=minbuttons[0]
#NextValidValue is One more than the last added value, since you have to buy a distinct number of buttons
NextValidValue = minbuttons[0]+1
for i in xrange(1,nclusters):
    #NextValidValue is the max between the former NextValidValue and a[i] 
    #which is the minimum number of buttons that need to be bought
    NextValidValue=max(NextValidValue,minbuttons[i])
    s+=NextValidValue
    NextValidValue+=1
print s

#Hope my code is clean enough! Do you understand it?
