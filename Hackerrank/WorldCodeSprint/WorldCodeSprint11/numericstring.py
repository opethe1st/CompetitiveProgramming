def convert2base(numb, b, m):
    ans = 0
    for digit in numb:
        ans = ans * b + int(digit)
        ans %= m
    return ans


def convert2baseWithPrev(prevnum, num, start, b, k, m):
    ans = prevnum - start * pow(b, (k - 1), m)
    ans *= b
    ans += num
    return ans % m


def getMagicNumber(s, k, b, m):
    # Complete this function
    #  letters = list(s)
    ans = 0
    numb = s[:k]
    prevnum = convert2base(numb, b, m)
    #  print prevnum
    ans += prevnum % m
    for i in xrange(k, len(s)):
        prevnum = convert2baseWithPrev(
            prevnum, int(s[i]), int(s[i - k]), b, k, m)
        ans += prevnum
    return ans


print getMagicNumber('12212', 3, 3, 5)
