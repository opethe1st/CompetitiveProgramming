from unittest import TestCase


def solution(arr, brr):
    assert len(arr) == len(brr)
    n = len(arr)
    minSwap = [[float('inf') for i in range(2)] for j in range(n)]
    minSwap[n-1][0] = 0
    minSwap[n-1][1] = 1
    for i in reversed(range(n-1)):
        minSwap[i][0] = min(
            minSwap[i+1][0] if arr[i]<arr[i+1] and brr[i]<brr[i+1] else float('inf'),
            minSwap[i+1][1] if arr[i]<brr[i+1] and brr[i]<arr[i+1] else float('inf'),
            )
        minSwap[i][1] = 1 + min(
            minSwap[i+1][1] if arr[i]<arr[i+1] and brr[i]<brr[i+1] else float('inf'),
            minSwap[i+1][0] if arr[i]<brr[i+1] and brr[i]<arr[i+1] else float('inf'),
        )
    return min(minSwap[0]) if min(minSwap[0]) != float('inf') else -1


class TestSolution(TestCase):

    def test_1(self):
        ans = solution(arr=[1, 6, 3, 4, 5], brr=[1, 2, 13, 14, 15])
        self.assertEqual(ans, 1)

    def test_2(self):
        ans = solution(arr=[1, 6, 3, 4, 5, 16], brr=[1, 2, 13, 14, 15, 6])
        self.assertEqual(ans, 2)

    def test_3(self):
        ans = solution(arr=[1, 6, 3, 4, 5, 16, 7], brr=[1, 2, 13, 14, 15, 6, 17])
        self.assertEqual(ans, 2)
