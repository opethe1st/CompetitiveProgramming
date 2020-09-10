"""
Between every pair of runners, find out when they meet
if they meet at all.
sort these times, (time_meet, (a, b))
assume the first athlete is infected and then run through the times.
assume the second athlete is infected and then run through the times
and so on.
and find the one with the minimum number of people infected.
"""


def get_meet_time(a, b, velocities):
    if a < b and velocities[a] > velocities[b]:
        return (b - a) / (velocities[a] - velocities[b])
    elif a > b and velocities[a] < velocities[b]:
        return (a-b) / (velocities[b] - velocities[a])
    return None


def solution(velocities):
    n = len(velocities)
    meet_times = []
    for person in range(n):
        for other in range(person+1, n):
            meet_time = get_meet_time(person, other, velocities)
            if meet_time is not None:
                meet_times.append((meet_time, (person, other)))
    meet_times.sort()
    min_infected = float('inf')
    max_infected = -float('inf')

    for person in range(n):
        infected = set([person])
        for _, (person, other) in meet_times:
            if person in infected:
                infected.add(other)
            if other in infected:
                infected.add(person)
        min_infected = min(min_infected, len(infected))
        max_infected = max(max_infected, len(infected))
    return min_infected, max_infected


T = int(input())
for i in range(T):
    N = int(input())
    velocities = list(map(int, input().split()))
    min_infected, max_infected = solution(velocities)
    print(f'{min_infected} {max_infected}')
