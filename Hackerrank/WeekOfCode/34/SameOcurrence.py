def preprocess(A):


def query(A, x, y):
    countx = 0
    county = 0
    difference = {}
    for i in xrange(len(A)):
        if A[i] == x:
            countx += 1
        if A[i] == y:
            county += 1
        difference[countx - county] = difference.get(countx - county, 0) + 1
        #difference[county-countx] = difference.get(county-countx, 0)+1
    ans = 0
    # print difference
    for diff in difference:
        ans += difference[diff] * (difference[diff] - 1) / 2
    if 0 in difference:
        ans += difference[0]
    return ans


if __name__ == "__main__":
    n, q = raw_input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = map(int, raw_input().strip().split(' '))
    for a0 in xrange(q):
        x, y = raw_input().strip().split(' ')
        x, y = [int(x), int(y)]
        # Write Your Code Here
        print query(arr, x, y)
