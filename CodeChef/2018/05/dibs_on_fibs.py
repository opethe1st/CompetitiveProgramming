FIBONACCI_COUNT = 100050
MODULO = 1000000007
# print('{0:.2E}'.format(MODULO))

fib = [0]*FIBONACCI_COUNT

fib[0] = 1
fib[1] = 1
for i in range(2, FIBONACCI_COUNT):
    fib[i] = (fib[i-1] + fib[i-2])%MODULO

def solution(M, N, aArr, bArr):
    if N == 1:
        return M*sum(aArr)
    elif N == 2:
        return M*sum(bArr)
    return M*(sum(bArr)*fib[N-2] + sum(aArr)*fib[N-3])
T = int(input())

for _ in range(T):
    M, N = list(map(int, input().split()))
    aArr = list(map(int, input().split()))
    bArr = list(map(int, input().split()))
    ans = solution(M, N, aArr, bArr)
    print(ans%MODULO)
