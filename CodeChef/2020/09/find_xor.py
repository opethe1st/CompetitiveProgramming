def ask_questions(n):
    print("1 1")
    k_zero = int(input())
    if k_zero == -1:
        raise Exception("cant ask with k == zero")
    last_digit = (n - k_zero) % 2
    reverse_digits = [last_digit]
    n_digits = 20
    for digit in range(1, n_digits):
        # ask question
        print(f"1 {((1<<n_digits)-1) - (1<<digit)  - 1}")
        # get the answer
        ans = int(input())
        x = k_zero + ans
        double_number_ones = x - n * (
            ((((1 << n_digits) - 1) ^ (1 << digit)))
        )
        reverse_digits.append(((double_number_ones >> (digit + 1))) & 1)
    ans = sum(reverse_digits[i] << i for i in range(len(reverse_digits)))
    print(f"2 {ans}")
    is_correct = int(input())
    if is_correct != 1:
        raise Exception("incorrect")


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        ask_questions(N)
