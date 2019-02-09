# cook your dish here
T = int(input())

for _ in range(T):
    N = int(input())
    A = map(int, input().split())
    print(sum(A) +1 - N)
