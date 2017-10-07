def solution(a):
    ps = a[0]
    ss = sum(a)
    mini = ps + ss
    minindex = 0
    for i in range(1, len(a)):
        print(ps+ss)
        ps += a[i]
        ss -= a[i - 1]
        if mini > ps + ss:
            mini = ps + ss
            minindex = i
    return minindex


def solution2(a):
    mod = (1 << 32)
    ps = a[0] % mod
    ss = sum(a) % mod
    mini = (ps + ss) % mod
    minindex = 0
    for i in range(1, len(a)):
        ps += a[i]
        ss -= a[i - 1]
        if mini > (ps + ss) % mod:
            mini = (ps + ss) % mod
            minindex = i
    return minindex


def counterTest(n):
    val = ((1 << 32) - 2*(10**5))//(n-1)
    arr = [val] * n
    d = (1 << 32) - 2*(10**5)-val*(n-1)
    # arr[2] += d
    for i in range(d):
        arr[i+1] += 1
    arr[0] = 10**5
    assert sum(arr)+arr[0] == (1 << 32)
    return arr


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        testcase = counterTest(N)
        for val in testcase:
            print(val, end=' ')
        print()
