A = range(1,101)
killed = 0
newA = A[:]
while killed<99:
    count = 0
    for n in A:
        count+=1
        if count%2==0:
            newA.remove(n)
            killed+=1
    if count>1 and count%2==1:
        newA = newA[1:]
        killed+=1
    print newA,"len",len(newA)
    A = newA[:]
