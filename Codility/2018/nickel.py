def solution(arr):
    contiguous_zeros = []
    count = 0
    for item in arr:
        if item is False:
            count += 1
        elif item is True:
            if count:
                contiguous_zeros.append(count)
            count = 0
    if count:
        contiguous_zeros.append(count)
    sum_pascal = lambda x: x*(x+1)//2
    sum_false_nodes = 0
    for item in contiguous_zeros:
        sum_false_nodes += sum_pascal(item)
    ans = sum_pascal(len(arr)) - sum_false_nodes
    return ans if ans <= 1000000000000 else 1000000000000
