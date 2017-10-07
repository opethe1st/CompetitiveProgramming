def maxNumber(n, b):
    x = n/(2*b)
    # max((x*n - x**2) / b , ((x+1)*n - (x+1)**2) / b)
    f = (n - x*b)*x
    x += 1
    g = (n - x*b)*x
    #x += 1
    #h = (n - x*b)*x
    #print f, g, h
    return max(f, g)

T = input()
for _ in xrange(T):
    n, b = map(int, raw_input().split())
    print maxNumber(n, b) 