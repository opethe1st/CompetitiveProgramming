
def solution(s):
    stack = []
    operators = ['+', '-', '*', '/', '^']
    res = []
    for l in s:
        if l in operators:
            stack.append(l)
        elif l == ')':
            res.append(stack[-1])
            stack.pop(-1)
        elif l == '(':
            pass
        else:
            res.append(l)
    return "".join(res)

# assert solution('(a+t)*((b+(a+c))^(c+d)))') == 'at+bac++cd+^*'
T = input()
for _ in xrange(T):
    s = raw_input()
    print solution(s)