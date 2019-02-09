import sys

T = int(input())
sys.stdout.flush()

for _ in range(T):

    print('Q 0 0')
    d1 = int(input())
    sys.stdout.flush()

    print('Q 0 1000000000')
    d2 = int(input())
    sys.stdout.flush()
    y1y2 = d1 - d2 + 1000000000

    print(f'Q 0 {y1y2//2}')
    a1 = int(input())
    sys.stdout.flush()
    print(f'Q 0 {y1y2 - y1y2//2}')
    a2 = int(input())
    sys.stdout.flush()

    x1 = min(a1, a2)
    y1 = d1 - x1
    y2 = x1 + 1000000000 - d2
    y1, y2 = min(y1, y2), max(y1, y2)

    print(f'Q 1000000000 {y1y2//2}')
    b1 = int(input())
    sys.stdout.flush()
    print(f'Q 1000000000 {y1y2 - y1y2//2}')
    b2 = int(input())
    sys.stdout.flush()
    x2 = 1000000000 - min(b1, b2)

    x1, x2 = min(x1, x2), max(x1, x2)

    print(f'A {x1} {y1} {x2} {y2}')
    a = int(input())
    sys.stdout.flush()
    if a < 0:
        raise Exception('wrong answer')
