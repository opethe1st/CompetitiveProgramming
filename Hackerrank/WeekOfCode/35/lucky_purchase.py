#!/bin/python3

if __name__ == "__main__":
    correctChoiceValue = float('inf')
    n = int(input().strip())
    for a0 in range(n):
        name, value = input().strip().split(' ')
        name, value = [str(name), str(value)]
        if value.count('7') == value.count('4') and value.count('7') * 2 == len(value):
            if correctChoiceValue > int(value):
                correctChoiceValue = int(value)
                correctChoiceName = name
    if correctChoiceValue == float('inf'):
        print(-1)
    else:
        print(correctChoiceName)
