def f(num):
    s = 0
    for n in xrange(1,num+1):
        s+=(15 * 16**(n-1) - 43 * 15**(n-1) + 41 * 14**(n-1) - 13**n)
    return "{:X}".format(s),s

print f(16)