""" Project Euler 152"""
import fractions

f = [fractions.Fraction(1,i*i) for i in xrange(2,101)]
f = [1.0/float(i*i) for i in xrange(2,101)]
#print f

#You are given N and D. result should be the number of ways of writing 1/D as a sum of square fractions less than N+1

#use a backtracking algorithm

Solution = []
def backtrackDFS(goal,possibleChoices,pathSoFar,selected):
    print goal,possibleChoices,pathSoFar,selected
    if abs(pathSoFar-goal)<10e-6:
        #print pathSoFar, goal, selected
        #print 'here2'
        print selected
        Solution.append(set(selected))
        return
    else:
        if sum(possibleChoices)<(goal-pathSoFar):
            #print 'here'
            return
        for element in possibleChoices:
            #print 'element',element,possibleChoices
            pathSoFar+=element
            if pathSoFar>goal:
                pathSoFar-=element
                continue
            possibleChoices.remove(element)
            selected.add(element)
            #print pathSoFar,selected
            backtrackDFS(goal,possibleChoices,pathSoFar,selected)
            possibleChoices.add(element)
            selected.remove(element) 
print f[:44]
backtrackDFS(0.5,set(f[:44]),0,set())
print Solution