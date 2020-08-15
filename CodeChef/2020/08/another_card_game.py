"""
Power of a positive integer is the sum of digits of that integer.
power(13) = 1+3
chef and rick - randomly generated positive integers - received final power
generate a positive integer such that it's power is equal to his final power

need to find the smallest number of digit that a number with that power could have for chef and rick
if chef is smaller then chef wins and return the number of digits
"""
import math


def smallest_digit_with_power(power):
    return math.ceil(power/9)


def solution(chef, rick):
    smallest_chef = smallest_digit_with_power(chef)
    smallest_rick = smallest_digit_with_power(rick)
    if smallest_chef < smallest_rick:
        return 0, smallest_chef
    else:
        return 1, smallest_rick

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        chef, rick = map(int, input().split())
        winner, no_of_digits = solution(chef, rick)
        print(f'{winner} {no_of_digits}')
