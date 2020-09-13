
def fair_distribution(n, k):
    sum_a = 0
    sum_b = 0

    in_a = ['1' for i in range(n)]
    for i in range(n, 0, -1):
        if sum_a < sum_b:
            sum_a += i**k
            in_a[i-1] = '0'
        else:
            sum_b += i**k

    return abs(sum_a - sum_b), "".join(in_a)


if __name__ == '__main__':
    K = int(input())
    T = int(input())
    for _ in range(T):
        N = int(input())
        min_diff, distribution = fair_distribution(N, K)
        print(min_diff)
        print(distribution[:10])
