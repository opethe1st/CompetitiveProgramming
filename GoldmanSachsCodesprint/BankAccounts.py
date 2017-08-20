def feeOrUpfront(n, k, x, d, p):
    # calculate fee
    fee = 0
    for payment in p:
        fee += max(k, x/100.0*payment)
    # compare with upfront payment
    if fee <= d:
        return "fee"
    else:
        return "upfront"

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, k, x, d = raw_input().strip().split(' ')
        n, k, x, d = [int(n), int(k), int(x), int(d)]
        p = map(int, raw_input().strip().split(' '))
        result = feeOrUpfront(n, k, x, d, p)
        print result