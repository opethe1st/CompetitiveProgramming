def isCorrect(arr, r):
    arr = list(arr)
    if len(arr) < 3:
        return True
    if arr[0] < arr[1]:
        mini = arr[0]
        maxi = float('inf')
    else:
        mini = -float('inf')
        maxi = arr[0]
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] < arr[i+1]:
            if mini > arr[i]:
                return False
            mini = arr[i]
        elif arr[i-1] > arr[i] > arr[i+1]:
            if maxi < arr[i]:
                return False
            maxi = arr[i]
        elif (arr[i-1] < arr[i]) and (arr[i+1] < arr[i]):
            if maxi < arr[i]:
                return False
            maxi = arr[i]
        elif (arr[i-1] > arr[i] and arr[i+1] > arr[i]):
            if mini > arr[i]:
                return False
            mini = arr[i]
        else:
            raise Exception('shouldnt get here')
        if not(mini <= arr[i] <= maxi):
            return False
    if not(mini <= arr[-1] <= maxi):
        return False
    return True

# print(isCorrect([5123, 3300, 783, 1111, 890], 890))
T = int(input())

for _ in range(T):
    N, R = map(int, input().split())
    arr = map(int, input().split())
    if isCorrect(arr=arr, r=R):
        print('YES')
    else:
        print('NO')
