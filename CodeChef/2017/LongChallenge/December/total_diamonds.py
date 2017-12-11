# pylint: disable=R0903, missing-docstring

def number_of_diamonds(room_number):
    even_sum, odd_sum = 0, 0
    while room_number:
        digit = room_number%10
        if digit%2:
            even_sum += digit
        else:
            odd_sum += digit
        room_number //= 10
    return abs(even_sum - odd_sum)

#simple tests
assert number_of_diamonds(room_number=3316) == 1
assert number_of_diamonds(room_number=0) == 0
assert number_of_diamonds(room_number=10) == 1

DIAMONDS = [number_of_diamonds(room_number=room_number) for room_number in range(2000001)]
PREFIX_SUM = [0] * 2000001
for i in range(1, 2000001):
    PREFIX_SUM[i] = PREFIX_SUM[i-1]+DIAMONDS[i]

assert PREFIX_SUM[4] == 10

cache = {}
cache[1] = 2
cache[2] = 12
def total_diamonds(num):
    if num in cache:
        return cache[num]
    else:
        cache[num] = 2*(PREFIX_SUM[2*num-1] - PREFIX_SUM[num]) + DIAMONDS[2*num] + total_diamonds(num=(num-1))
    return cache[num]

for i in range(1, 1000001):
    total_diamonds(num=i)

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(total_diamonds(num=N))
