# Array of numbers, from 1 to 100
A = range(1, 101)
# Number of people killed
killed = 0
newA = A[:]
while killed < 99:
    # use this at the beginning of the round to count, odd numbered people
    # kill even numbered people
    count = 0
    for n in A:
        count += 1
        if count % 2 == 0:
            # kill person numbered n
            newA.remove(n)
            killed += 1
    # at the end of the loop, check if the last person has to kill the first
    # in front
    if count > 1 and count % 2 == 1:
        newA = newA[1:]
        killed += 1
    print newA, "len", len(newA)
    A = newA[:]
