
def solution(N, A):
    counters = [0 for i in range(N)]
    maxCounter = 0  # max counter from the last time, every counter was set to the max.
    currentMax = 0  # the max value in a ny counter at this iteration
    for a in A:
        if 0 < a <= N:
            counters[a-1] = max(maxCounter, counters[a-1])  # checks if 
            counters[a-1] += 1
            currentMax = max(currentMax, counters[a-1])
        elif a == N+1:
            maxCounter = currentMax

    for i in range(N):
        counters[i] = max(maxCounter, counters[i])
    return counters

print solution(6, [1, 2, 3, 1, 1, 3, 3, 1])
