
def generate_cake(firstColour, secondColour, width, breadth):
    resArr = [[0 for j in range(width)] for i in range(breadth)]
    for i in range(breadth):
        for j in range(width):
            if (i+j)%2 == 0:
                resArr[i][j] = firstColour
            else:
                resArr[i][j] = secondColour
    return ["".join(row) for row in resArr]

def compare(arr1, arr2):
    assert len(arr1)==len(arr2)
    assert len(arr1[0])==len(arr2[0])
    n = len(arr1)
    m = len(arr1[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if arr1[i][j]=='R' and arr2[i][j]=='G':
                ans += 5  # replacing red with green is 5
            elif arr1[i][j]=='G' and arr2[i][j]=='R':
                ans += 3  # replacing green with red is 3
    return ans

T = int(input())

for _ in range(T):
    n, m = list(map(int, input().split()))
    arr = []
    for j in range(n):
        arr.append(input().strip())
    redCake = generate_cake(firstColour='R', secondColour='G', width=m, breadth=n)
    greenCake = generate_cake(firstColour='G', secondColour='R', width=m, breadth=n)
    print(min(compare(arr1=arr, arr2=redCake), compare(arr1=arr, arr2=greenCake)))
