"""
Link to (question)[https://www.codechef.com/SEPT20B/problems/CRDGAME2]

The key idea here is that the maximum never changes the pile it belongs to
while every other number will change the pile it belongs to and reduce by 1
So we can focus on the number of maximum values.
if the number of maximum values is odd, it doesn't matter
how the distribution is made, there will always be a winner since the numbers
less than the maximum will reduce to zero and the sum of piles that contain
just the maximum will always be different i.e a winner exist.
the only case where they could be a draw is when the maximum occurs an
even number of times. So we just need to compute the number of possible ways
this could happen.
That is combinations(n_max, n_max//2)*2**(len(cards) - n_max)
So to find the distributions that cant end in draws we substract this
from 2**len(card)
"""
from collections import Counter

MOD = 1_000_000_007

factorial = [1 for _ in range(100001)]
for i in range(1, 100001):
    factorial[i] = (factorial[i-1] * i) % MOD


def inverse(x):
    return pow(x, MOD-2, MOD)


def combination(n, r):
    return (factorial[n] * inverse(factorial[r]) ** 2) % MOD


def number_of_distributions_with_winner(cards):
    max_value = max(cards)
    counter = Counter(cards)
    if counter[max_value] % 2 == 1:
        return pow(2, len(cards), MOD)
    else:
        return pow(2, len(cards), MOD) - combination(
            counter[max_value], counter[max_value] // 2
        ) * pow(2, len(cards) - counter[max_value], MOD)


T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(map(int, input().strip().split()))
    print(number_of_distributions_with_winner(cards) % MOD)
