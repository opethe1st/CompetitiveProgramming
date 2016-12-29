"""Implementation of a backtracking algorithm that prints the permutations of a given set.
"""
import time
def findperm(Left,PickedSoFar,NumLeft):
    if NumLeft==6:
        Solutions.append("".join(PickedSoFar[:]))
        return 
    else:
        for i in xrange(len(Left)): #could have made this just iterate from 0 to Nleft-1. they used a boolean array. smart
            if Left[i]==False:
                PickedSoFar.append(items[i])
                NumLeft-=1
                Left[i] = True
                findperm(Left,PickedSoFar,NumLeft)
                PickedSoFar.pop(-1)
                NumLeft+=1
                Left[i] = False

def permutation(v_items):
    global Solutions
    global items
    items = v_items 
    Solutions = []
    Left = [False]*len(items)
    PickedSoFar = []
    NumLeft = len(items)
    findperm(Left,PickedSoFar,NumLeft)
    #print len(Solutions)
    return Solutions

#How do I optimise to not create a new Left list at every level. Use range instead?


        

start = time.time()
print permutation("UBBGELHARJL")