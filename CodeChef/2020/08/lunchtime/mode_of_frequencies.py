"""
Clarify
A of size N. find the mode of the frequencies of the numbers. if multiple modes return the smallest one
"""
from collections import Counter


def mode_of_frequencies(A):
    frequencies = Counter(Counter(A).values())
    max_frequency = max(frequencies.values())
    max_value = float('inf')
    for val, frequency in frequencies.items():
        if frequency == max_frequency and val < max_value:
            max_value = val
    return max_value


T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(mode_of_frequencies(A))
