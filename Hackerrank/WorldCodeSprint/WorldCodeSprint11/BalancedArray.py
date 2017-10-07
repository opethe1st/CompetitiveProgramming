def solve(A):
    left = sum(A[:len(A)/2])
    right = sum(A) - left
    minidiff = abs(left - right)
    return minidiff

print solve([20, 10])
print solve([1, 2, 5, 2, 4, 2])