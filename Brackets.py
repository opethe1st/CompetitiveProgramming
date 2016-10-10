"""
Problem from - https://codility.com/programmers/lessons/7-stacks_and_queues/brackets/
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

int solution(char *S);
that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
"""

def solution(s):
    #print s,
    stack = []
    for l in s:
        #print l,stack
        if l=='(' or l=='{' or l == '[':
            stack.append(l)
        elif l==')':
            if len(stack)>0 and stack[-1]=='(':
                stack.pop(-1)
            else:
                return 0
        elif l==']':
            if len(stack)>0 and stack[-1]=='[':
                stack.pop(-1)
            else:
                return 0
        elif l=='}':
            if len(stack)>0 and stack[-1]=='{':
                stack.pop(-1)
            else:
                return 0
        #print l,stack
    if not stack or len(s)==0:
        return 1
    else:
        return 0

print solution('{[()()]}')
