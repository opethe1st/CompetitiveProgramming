from fractions import Fraction
Modulo = int(10**9 + 7)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
def FFT(A, w):
    """A is a polynomial of degree 2^k=n. (pad with zeros if necessary), w is
    the kth root of unity. This function takes the coefficent expansion of the
    polynomical and returns the value representation of the polynomial
    """
    if len(A) == 1:
        return A
    Aodd = [A[i] for i in xrange(1, len(A), 2)]
    Aeven = [A[i] for i in xrange(0, len(A), 2)]
    Aoddvalues = FFT(Aodd, w**2)
    Aevenvalues = FFT(Aeven, w**2)
    Ans = []
    for i in xrange(len(A)/2):
        Ans.append(Aevenvalues[i] + w**i * Aoddvalues[i])
    for i in xrange(len(A)/2):
        Ans.append(Aevenvalues[i] - w**i * Aoddvalues[i])
    return Ans

def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


def power(a, poly, i):
    ans = 0
    count = len(a) - 1
    while count >= 0:
        if poly & 1:
            ans += a[count]**i
        count -= 1
        poly >>= 1
    return ans


# Refactor.. make poly a bit set, possibly need 5000 bits
# then form
symmetricPolyDic = dict()


def symmetricPoly(a, poly, degree):
    if (poly, degree) in symmetricPolyDic:
        return symmetricPolyDic[(poly, degree)]
    e = [0] * (degree + 1)
    e[0] = 1
    for k in xrange(1, degree + 1):
        for i in xrange(1, k + 1):
            e[k] += (-1)**(i - 1) * symmetricPoly(a,
                                                  poly, degree - i) * power(a, poly, i)
        e[k] /= k
        symmetricPolyDic[(poly, k)] = e[k]
    # print poly, degree, e[degree]
    symmetricPolyDic[(poly, degree)] = e[degree]
    return e[degree]
# print symmetricPoly([1]*5, 1)


def solution(c, a):
    # print c,a
    c = list(reversed(c))
    ans = 0
    for i in xrange(len(c)):
        val = 0
        mina = min(a[i], a[i + 1])
        maxa = max(a[i], a[i + 1])
        for x in xrange(mina + 1, maxa + 1):
            val += 1 / Fraction(x)
        val *= c[i] / Fraction(maxa - mina)
        # print val
        ans += val
    return ans


def multiply(roots):
    def multiplyRoot(p1, p2):
        ans = [0] * (len(p1) + len(p2) - 1)
        for i in xrange(len(p1)):
            for j in xrange(len(p2)):
                ans[i + j] += p1[i] * p2[j]
        return ans
    ans = [1]
    for root in roots:
        ans = multiplyRoot(ans, [1, root])
    return ans

# print multiply([1, 1])
# print multiply([1, 1, 1, 1])
# print multiply([1, 1, 1, 1, 1])


def rationalSums(n, a, b):
    # Complete this function
    # Augmented matrix
    # print len(a), n
    A = [[0 for i in xrange(n)] for i in xrange(n - 1)]
    Columns = [[0 for i in xrange(n - 1)] for i in xrange(n - 1)]
    myseta = set(a)
    for i in xrange(n - 1):
        myseta.remove(a[i])
        myseta.remove(a[i+1])
        Columns[i] = multiply(myseta)
        myseta.add(a[i])
        myseta.add(a[i+1])
    for i in xrange(n - 1):
        for j in xrange(n - 1):
            A[i][j] = Fraction(Columns[-j-1][i]) # Fraction(symmetricPoly(a, seta, i))
            # print A[i][j], Columns[-j-1][i]
        A[i][n - 1] = b[n - i - 2]
    # print A
    c = gauss(A)
    print c
    ans = solution(c, a)
    # print c, ans
    return ans.numerator * modinv(ans.denominator, Modulo)


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
result = rationalSums(n, a, b) % Modulo
print(result)
