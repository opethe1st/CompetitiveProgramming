T = input()

for _ in xrange(T):
    u, v, x = map(int, raw_input().split())
    print "%.9f" % (x/float(u+v))