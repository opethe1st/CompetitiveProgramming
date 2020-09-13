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
