import sys
import time
def cannotMove(u):
    if R[u]==0:
        return True
    else:
        return False

def isDestinationReached(u,direction):
    print u,s,t,direction
    if s<t:
        if direction==True and u>=t:
            return True
        elif direction==False and t<=u:
            return True
        else:
            return False
    else:
        if direction==False and u<=t:
            return True
        elif direction==True and t>=u:
            return True
        else:
            return False
def circularWalk(n, s, t, r_0, g, seed, p):
    # Complete this function
            
    stack=[(s,0,True)]
    while stack:
        #print stack
        #print 
        u,time,direction = stack.pop(0) #my current position
        visited[u]=True
        if cannotMove(u): #if I cannot move from this position, try another position on the stack
            continue 
        #if isDestinationReached(u,direction): #if the destination can be reached from this position
        #    return time+1 #then return the current time plus one!
        if u==t:
            return time
        else:
            #cannot be reached in one step, then save all the positions that can be reached from current position
            #only if they haven't been visited earlier
            maxval = 0
            maxi=u
            for d in xrange(-R[u],0):  #Backwards
                if not visited[(u+d)%n]:  
                    stack.append(((u+d)%n, time+1,False))  #I need to append just the node that goes the furthest
                                                        #Among the new nodes to consider so find max (u+d)%n+R[(u+d)%n]
            for d in xrange(R[u]+1):
                if not visited[(u+d)%n]: #Forwards
                    stack.append(((u+d)%n, time+1,True))
    return -1


start = time.time()

n, s, t = 1000,0,500#raw_input().strip().split(' ')
n, s, t = [int(n), int(s), int(t)]
r_0, g, seed, p = 1, 3, 4, 7#raw_input().strip().split(' ')
r_0, g, seed, p = [int(r_0), int(g), int(seed), int(p)]

visited=[False]*n
R = [0]*n 
R[0]=r_0
for i in range(1,n):
    R[i]=(R[i-1]*g+seed)%p

#print R

result = circularWalk(n, s, t, r_0, g, seed, p)
print(result)
print time.time()-start