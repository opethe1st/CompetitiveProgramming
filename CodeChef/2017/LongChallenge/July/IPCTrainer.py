import heapq


def minimumSadness(Trainers, D):
    # print Trainers
    pQ = []
    t = 0
    for d in xrange(1, D+1):  # simulate each day
        while t < len(Trainers) and Trainers[t][0] == d:
            heapq.heappush(pQ, (Trainers[t][1], Trainers[t][2]))
            t += 1
        if pQ != []:
            val, c = heapq.heappop(pQ)
            if c > 1:
                heapq.heappush(pQ, (val, c-1))
    sadnessLeft = 0
    for val, c in pQ:
        sadnessLeft -= val*c
    return sadnessLeft

T = input()
for _ in xrange(T):
    N, D = map(int, raw_input().split())
    Trainers = []
    for _ in xrange(N):
        d, t, s = map(int, raw_input().split())
        Trainers.append((d, -s, t))
    Trainers.sort()
    print minimumSadness(Trainers, D)