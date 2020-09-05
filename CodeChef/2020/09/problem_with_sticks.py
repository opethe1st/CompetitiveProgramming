"""
N stick holders labeled 1 to N in a row on the ground.
initial height of a stick is heights[i]
"""


def solution(heights):
    unique_heights = set(heights)
    return len(unique_heights) - int(0 in heights)


T = int(input())
for i in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    print(solution(heights))
