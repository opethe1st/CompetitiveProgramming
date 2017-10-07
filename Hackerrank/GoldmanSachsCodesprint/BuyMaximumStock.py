def buyMaximumProducts(n, k, a):
    stocks = []
    for i in xrange(len(a)):
        stocks.append((a[i], i+1))
    stocks.sort()
    count = 0
    for stock in stocks:
        price, number = stock[0], stock[1]
        if price*number <= k:
            count += number
            k -= price*number
        else:
            number = k/price
            count += number
            k -= price*number
            break
    return count


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    k = long(raw_input().strip())
    result = buyMaximumProducts(n, k, arr)
    print result
