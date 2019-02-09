
def get_factors_less_than_26(num):
    return [i for i in range(1, 27) if (num % i) == 0]


def minimum_op_to_be_balanced(string):
    charToCount = {}
    for letter in string:
        charToCount[letter] = charToCount.get(letter, 0) + 1

    counts = sorted(list(charToCount.values()), reverse=True)
    minNumberOfOp = float('inf')
    for factor in get_factors_less_than_26(num=len(string)):
        num = len(string) // factor

        currentMinNumberOfOp = 0
        for count in counts[:factor]:
            # change only the ones that are greater, they will be converted to the ones that are less
            if count > num:
                currentMinNumberOfOp += (count - num)

        # need to convert the rest to the first factor characters
        currentMinNumberOfOp += sum(counts[factor:])

        if currentMinNumberOfOp < minNumberOfOp:
            minNumberOfOp = currentMinNumberOfOp

    return minNumberOfOp


T = int(input())

for _ in range(T):
    string = input()
    print(minimum_op_to_be_balanced(string=string))
