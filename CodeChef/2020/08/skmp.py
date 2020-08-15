# This solution thanks to Bolu
from collections import Counter


class TrueWhileLeftNotGreater(object):
    def __init__(self):
        self.__ever_false = False

    def __call__(self, left, right):
        if self.__ever_false:
            return False
        # return not self.__ever_false := not left <= right
        self.__ever_false = not left <= right
        return not self.__ever_false


class TrueWhileLeftLess(object):
    def __init__(self):
        self.__ever_false = False

    def __call__(self, left, right):
        if self.__ever_false:
            return False
        # return not self.__ever_false := not left <= right
        self.__ever_false = not left < right
        return not self.__ever_false


# too general for the use case, but in the spirit of "no raw loops" :D
def merge(left, right, pred):
    left_iter = iter(left)
    right_iter = iter(right)

    left_next = next(left_iter, None)
    right_next = next(right_iter, None)

    while left_next and right_next:
        if pred(left_next, right_next):
            yield left_next
            left_next = next(left_iter, None)
        else:
            yield right_next
            right_next = next(right_iter, None)

    while left_next:
        yield left_next
        left_next = next(left_iter, None)

    while right_next:
        yield right_next
        right_next = next(right_iter, None)


def has_decreasing_prefix(string):
    for i in range(len(string) - 1):
        if string[i] < string[i + 1]:
            return False
        if string[i] > string[i + 1]:
            return True
    return True


def smallest_anagram_with_pattern(string, pattern):
    string_freq = Counter(string)
    pattern_freq = Counter(pattern)
    circum_freq = string_freq - pattern_freq
    circum_seq = sorted(circum_freq.elements())
    if has_decreasing_prefix(pattern):
        merge_pred = TrueWhileLeftLess()
    else:
        merge_pred = TrueWhileLeftNotGreater()
    merged_seq = merge(circum_seq, pattern, merge_pred)
    return "".join(merged_seq)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        string = input()
        pattern = input()
        print(smallest_anagram_with_pattern(string=string, pattern=pattern))
