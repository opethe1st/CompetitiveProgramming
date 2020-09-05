"""
N alien spaceships.
on_radar[i] - the time the ith spaceship appears on the radar
Each spaceship needs D time to reach the earth once it appears on the radar
Laser canon that can destroy ships. Once used, it needs cool down time that is set
before the first shot and is fixed thereafter. lower cooldown time increases energy
consumed by the cannon and vice-versa
ith spaceship should be shot between the times
[on_radar[i], on_radar[i]+D]
Ideas
Idea
Sort the on_radar array.
shoot the first ship as soon as it appears. find the latest time to shoot the next one - that's
when it is just as soon as it hits the earth. once that is done. shoot the next one,
maximum cooldown time would be the min of the difference between having to shoot consecutive ships
"""
"""
External solution
"""

# from decimal import *
def solve():
    n, d = (int(x) for x in input().split())

    arrivals = sorted([int(x) for x in input().split()])
    # getcontext().prec = 18

    def possible(cd):
        next_possible_ht = 0.
        for ship in arrivals:
            if next_possible_ht > ship + d:
                return False

            next_possible_ht = max(next_possible_ht + cd, ship + cd)
        return True



    r_op = 2. * 10**9
    l_cl = 0

    two = 2
    prec = .1**6.5

    count = 0
    while r_op - l_cl > prec:
        count += 1
        m = (l_cl + r_op) / two
        if possible(m):
            l_cl = m
        else:
            r_op = m

        if count > 100:
            break


    print("{:.7f}".format(l_cl))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
"""
----------------------------------------------------------------
"""
from collections import deque

def maximum_cool_down_time_possible(on_radar, travel_time):
    intervals = sorted(
        [(time, time + travel_time) for time in on_radar], key=lambda item: item[1]
    )
    queue = deque()
    current_interval = intervals[0]
    max_cool = -float('inf')
    i = 0
    while i < len(on_radar):
        while i < len(on_radar) and intervals[i][0] < current_interval[1]:
            queue.append(intervals[i])
            i += 1
        if queue:
            max_cool = max(max_cool, current_interval[1]-queue[0][0]/len(queue))
            queue.popleft()
            current_interval = queue[0] if queue else (-float('inf'), -float('inf'))
        i += 1

    return max_cool


T = int(input())
for _ in range(T):
    N, travel_time = map(int, input().split())
    on_radar = list(map(int, input().split()))
    print(maximum_cool_down_time_possible(on_radar=on_radar, travel_time=travel_time))
