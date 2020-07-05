

def power(num):
    ans = 0
    while num:
        ans += num%10
        num //= 10
    return ans

def solution(xs, ys):

    def points(x, y):
        if x < y:
            return 0
        else:
            return 1

    rounds = [(points(x, y), points(y, x)) for x, y in zip((power(x) for x in xs), (power(y) for y in ys))]
    xs_points = sum(point for point, _ in rounds)
    ys_points = sum(point for _, point in rounds)

    if xs_points < ys_points:
        return 1, ys_points
    elif xs_points == ys_points:
        return 2, xs_points
    else:
        return 0, xs_points

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N = int(input())
        A, B = [], []
        for _ in range(N):
            a, b = map(int, input().strip().split())
            A.append(a)
            B.append(b)

        winner, points = solution(A, B)
        print(f"{winner} {points}")
