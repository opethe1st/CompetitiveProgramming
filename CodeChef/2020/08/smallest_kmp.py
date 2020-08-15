"""
# Clarify
String S and string P. want to find P in S.
Find the lexicographically smallest anagram of S that contains P as a substring

# Ideas
## Idea 1 | complexity
hm. extract P from S. sort what is left and then insert p into the position it fits.
complexity - nlogn for the sorting?

S = "aaaaaaabc"
P = "abc"
----
# Testcases

"""
from collections import Counter


def padded_substring(letters, i, length):
    s = letters[i:i+length]
    if len(s) < length:
        s = s + 'z'
    return s


def smallest_anagram_with_pattern(string, pattern):
    letter_frequencies = Counter(string) - Counter(pattern)
    letters = "".join(sorted(letter_frequencies.elements()))

    start, end = 0, len(letters)
    while start < end:
        mid = (start + end)//2
        if pattern < padded_substring(letters, mid, len(pattern)):
            end = mid
        else:
            start = mid + 1
    insert_point = start
    ans = letters[:insert_point] + pattern + letters[insert_point:]
    assert len(ans) == len(string)
    return ans


# def smallest_anagram_with_pattern(string, pattern):
#     letter_frequencies = Counter(string) - Counter(pattern)
#     letters = "".join(sorted(letter_frequencies.elements()))
#     return min(letters[:i] + pattern + letters[i:] for i in range(len(letters) + 1))


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        string = input()
        pattern = input()
        print(smallest_anagram_with_pattern(string=string, pattern=pattern))
