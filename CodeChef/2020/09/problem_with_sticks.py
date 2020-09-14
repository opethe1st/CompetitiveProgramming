"""
Link to the (question)[https://www.codechef.com/SEPT20B/problems/TREE2]
The key insight is that at every cut, we are reducing the number of unique
heights and that we don't need to cut when the height is already zero.
So we can just count the number of unique heights that are not zero and we are done!
"""


def solution(heights):
    unique_heights = set(heights)
    return len(unique_heights) - int(0 in heights)


T = int(input())
for _ in range(T):
    N = int(input())
    heights = list(map(int, input().split()))
    print(solution(heights))
