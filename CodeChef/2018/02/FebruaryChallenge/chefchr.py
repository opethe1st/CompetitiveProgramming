def solution(s):
    lovely_sentences_count = 0
    for position in range(len(s)-3):
        if set(s[position: position+4]) == set('chef'):
            lovely_sentences_count += 1
    return "lovely {num}".format(num=lovely_sentences_count) if lovely_sentences_count else "normal"

T = int(input())

for _ in range(T):
    print(solution(s=input()))
