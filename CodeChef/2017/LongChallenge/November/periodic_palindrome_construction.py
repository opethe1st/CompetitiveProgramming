def getPalindrome(n, p):
    if p == 1:
        return 'impossible'
    elif p == 2:
        return 'impossible'
    else:
        q = int(n/p)
        ans = 'a'+'b'*(p-2)+'a'
        return ans*q

T = int(input())

for _ in range(T):
    n, p = list(map(int, input().split()))
    print(getPalindrome(n=n, p=p))
