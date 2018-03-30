from unittest import TestCase, main
from bisect import bisect_left

class Pair:

    def __init__(self, value, position):
        self.value = value
        self.position = position

    def __lt__(self, other):
        return self.value < other.value


def solution(A):
    prefix_sum = [0 for i in range(len(A)+1)]
    for i, value in enumerate(A):
        prefix_sum[i+1] = prefix_sum[i] + value

    greatest_sum_position_backwards = [Pair(value=prefix_sum[-1], position=len(A))]
    for position, value in reversed(list(enumerate(prefix_sum))):
        if greatest_sum_position_backwards[-1].value < value:
            greatest_sum_position_backwards.append(Pair(value=value, position=position))
    max_length = 0
    for left_position, value in enumerate(prefix_sum):
        right_position = greatest_sum_position_backwards[bisect_left(greatest_sum_position_backwards, Pair(value=value, position=left_position))].position
        if right_position and max_length < (right_position - left_position):
            max_length = (right_position - left_position)
    return max_length


class TestFunction(TestCase):

    def test_1(self):
        ans = solution(A=[1, 1, -1, -1, -1, -1, -1, 1, 1])
        self.assertEqual(ans, 4)

    def test_2(self):
        ans = solution(A=[-1, -1, 1, -1, 1, 0, 1, -1, -1])
        self.assertEqual(ans, 7)

    def test_3(self):
        ans = solution(A=[0, 0, 0])
        self.assertEqual(ans, 3)

    def test_4(self):
        ans = solution(A=[-1, -1, 1])
        self.assertEqual(ans, 2)

    def test_5(self):
        ans = solution(A=[-1, -1, -1])
        self.assertEqual(ans, 0)

    def test_6(self):
        ans = solution(A=[-1, 1])
        self.assertEqual(ans, 2)

    def test_7(self):
        ans = solution(A=[-1, -1])
        self.assertEqual(ans, 0)

    def test_8(self):
        ans = solution(A=[-1, -1, 0, 1, 1])
        self.assertEqual(ans, 5)

    def test_9(self):
        ans = solution(A=[1, 1, 1, 1, 1])
        self.assertEqual(ans, 5)

    def test_10(self):
        ans = solution(A=[-1, -1, -1, -1, 1])
        self.assertEqual(ans, 2)

    def test_11(self):
        ans = solution(A=[-1, -1, -1, 1, 1])
        self.assertEqual(ans, 4)

    def test_12(self):
        ans = solution(A=[-1, 1, -1, -1, 1])
        self.assertEqual(ans, 4)

if __name__ == '__main__':
    main()
