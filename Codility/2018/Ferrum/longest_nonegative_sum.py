from unittest import main, TestCase
from bisect import bisect_left

def solution(A):
    def find_max_non_negative_position(gs, i, s):
        keys = [val for val, pos in gs]
        return gs[bisect_left(keys, s)][1]
    prefix_sum = [0 for i in range(len(A)+1)]
    for i, value in enumerate(A):
        prefix_sum[i+1] = prefix_sum[i] + value
    # print(prefix_sum)
    greatest_sum_position_backwards = [(prefix_sum[-1], len(A))]
    for position, value in reversed(list(enumerate(prefix_sum))):
        if greatest_sum_position_backwards[-1][0] < value:
            greatest_sum_position_backwards.append((value, position))
    # print(greatest_sum_position_backwards)
    max_length = 0
    for i, s in enumerate(prefix_sum):
        # this is basically a find the left most position
        position = None
        # for v, p in greatest_sum_position_backwards:
        #     if v >= s:
        #         position = p
        #         break
        # assert (position == find_max_non_negative_position(gs=greatest_sum_position_backwards, i=i, s=s))
        position = find_max_non_negative_position(gs=greatest_sum_position_backwards, i=i, s=s)
        if position and max_length < (position - i):
            max_length = (position - i)
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

if __name__ == '__main__':
    # assert solution(A=[0, 0, 0]) == 3
    # print(solution(A=[1, 1, 1]))
    # assert solution(A=[1, 1, 1]) == 3
    # assert solution(A=[-1, 1, 1]) == 3
    # assert solution(A=[1, 1, 1]) == 3
    assert solution(A=[-1, -1, 1]) == 2
    # assert solution(A=[-1, -1, -1]) == 0
    main()
