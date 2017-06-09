from math import ceil
def solution(X,Y,B):
    return int(ceil((Y-X)/float(B)))

print solution (30,30,10)
print solution(20,50,30)
print solution(10,50,20)