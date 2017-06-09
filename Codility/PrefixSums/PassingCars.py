def solution(A):
    carsWest = 0
    carsPassingBy = 0
    for a in A:
        if a == 0:
            carsWest += 1
        else:
            carsPassingBy += carsWest
    if carsPassingBy > 1000000000:
        carsPassingBy = -1
    return carsPassingBy


# tests
print solution([0, 1, 0, 1, 1])
