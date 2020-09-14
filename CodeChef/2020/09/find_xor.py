"""
Link to (question)[https://www.codechef.com/SEPT20B/problems/FINXOR]
This required doing some maths to figure it out.

The key idea is that every time we make a query, we determine the value of a
single bit of the answer

You should note that based on the constraints of the problem, each
a[i] is max 20 digits.

Each query is the result of this expression.
    sum(x^k for x in a)
and we need to find
    ANSWER = reduce(lambda x, y: x^y, a)

A key insight is that in ANSWER, the ith bit is the parity of the sum
of the ith bit of each a[j]. So it suffices to find the the parity of the sum
of the ith bit to get the answer.
    ans = ∑∑a[i]&(1<<j) ^ k&(i<<j)
    where the summation is over j=0..19 and i=1..n

the first query is with k = 1 and the expression evaluates to
    query_1 = ∑∑a[i]&(1<<j) + ∑a[i]&(1<<0) ^ 1  where j=1..19
this since k&(1<<j) is zero for all the other bits except the 0th bit

for subsequent queries, k is choosen such that k is of the form 1*01*0
    ie. k = (1<<n_bits)-1) - (1<<l)  - 1
this is so that when it is added with query_1 and using the property that
    x ^ 1 + x ^ 0 = 1 where x is a single bit
we are able to compute
    a = ∑(∑(1<<j) + 2*a*(1<<l)) where j=0..n but j != l

then we subtract n * ((((1 << n_bits) - 1) ^ (1 << l))) from a
and get just
    2*a*(1<<l))
then bit shift l + 1 times and & 1 to get the parity
and save the answer.

Finally, get the integer from the bits.
"""


def ask_questions(n):
    print("1 1")
    query_1 = int(input())
    if query_1 == -1:
        raise Exception("invalid query")

    last_bit = (n - query_1) % 2
    reverse_digits = [last_bit]
    n_bits = 20
    for bit in range(1, n_bits):
        # ask question -
        # k is of the form 11111011110, in regex 1*01*0
        print(f"1 {((1<<n_bits)-1) - (1<<bit)  - 1}")
        # get the answer
        query_i = int(input())

        x = query_1 + query_i
        double_number_ones = x - n * (
            ((((1 << n_bits) - 1) ^ (1 << bit)))
        )
        reverse_digits.append(((double_number_ones >> (bit + 1))) & 1)
    query_i = sum(reverse_digits[i] << i for i in range(len(reverse_digits)))
    print(f"2 {query_i}")
    is_correct = int(input())
    if is_correct != 1:
        raise Exception("incorrect")


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        ask_questions(N)
