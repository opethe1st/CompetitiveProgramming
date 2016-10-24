# Enter your code here. Read input from STDIN. Print output to STDOUT
def convert210(a,base,digitsDic):
    #digits will be a dictionary.
    #a.strip()
    #print digitsDic
    n = 0
    for digit in a:
        if digit!=' ':
            n*=base
            n+=digitsDic[digit]
    return n

def convert2Base(n,base,reversedigitsDic):
    a =[]
    while n>0:
        lastdigit=n%base
        a.append(reversedigitsDic[lastdigit])
        n/=base
    a.reverse()
    return "".join(a)

base,digits = raw_input().split()
a = raw_input()
b = raw_input()
line = raw_input()
questionmarks = raw_input()

#processing
digitsDic={}
for i in xrange(len(digits)):
    digitsDic[digits[i]] = i
reverseDigitsDic = {}
for i in xrange(len(digits)):
    reverseDigitsDic[i] = digits[i]
print reverseDigitsDic
i = convert210(a,int(base),digitsDic)
j = convert210(b[1:],int(base),digitsDic)
k = i+j
c = convert2Base(k,int(base),reverseDigitsDic)

#print output
print base,digits
print a
print b
print line
print '',c