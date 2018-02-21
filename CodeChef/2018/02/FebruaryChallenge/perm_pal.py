import unittest

def solution(s):
    # can this be mase a palindrome? if not -1
    palindrome_test = 0
    for l in s:
        palindrome_test ^= (1<<(ord(l)-ord('a')))
    if (palindrome_test & (palindrome_test-1)):
        return -1
    else:
        permutation = [None for l in s]
        dict_of_list = {l:[] for l in set(s)}
        for i, l in enumerate(s):
            dict_of_list[l].append(i)
        center = None
        current_pos = 0
        for l in dict_of_list:
            if len(dict_of_list[l])%2 == 0:
                for i in range((len(dict_of_list[l]))//2):
                    permutation[current_pos] = dict_of_list[l][i]
                    permutation[-current_pos-1] = dict_of_list[l][-i-1]
                    current_pos += 1
            else:
                center = l
        if center:
            for i in range((len(dict_of_list[center])+1)//2):
                permutation[current_pos] = dict_of_list[center][i]
                permutation[-current_pos-1] = dict_of_list[center][-i-1]
                current_pos += 1
        return ' '.join(map(str, map(lambda x: x+1, permutation)))



T = int(input())

for _ in range(T):
    s = input()
    print(solution(s=s))

class TestSolution(unittest.TestCase):

    def test_1(self):
        s = 'asss'
        self.assertEqual(-1, solution(s))

    def test_2(self):
        s = 'asbbss'
        self.assertEqual(-1, solution(s))

    def test_3(self):
        s = 'rsasr'
        self.assertEqual('', solution(s))

    def test_4(self):
        s = 'ssss'
        self.assertEqual(None, solution(s))

    def test_5(self):
        s = 'sssss'
        self.assertEqual(None, solution(s))
