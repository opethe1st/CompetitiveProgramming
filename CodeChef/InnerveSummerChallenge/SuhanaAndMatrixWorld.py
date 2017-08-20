T = input()
for _ in xrange(T):
    M = input()
    a = M/3
    b = M/3 *2
    left = M%3
    if left == 1:
        a += 1
    elif left == 2:
        a+=1
        b+=1
    print a, b