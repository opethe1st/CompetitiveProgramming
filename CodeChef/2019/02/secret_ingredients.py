
def get_bit_set(string):
    a = 0
    for letter in string:
        a |= (1 << (ord(letter) - ord('a')))
    return a


def count_set_bits(num):
    count = 0
    while num:
        num = num & (num - 1)
        count += 1
    return count


T = int(input())

for _ in range(T):
    numberOfIngredients = int(input())

    ans = get_bit_set(input())
    for __ in range(numberOfIngredients - 1):
        ans &= get_bit_set(input())
    print(count_set_bits(ans))
