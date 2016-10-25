""""IEEEXtreme 10
""""
def convert210(a,base,digitsDic):
    "convert a in base with digitsDic set of digitsDic to a base 10 number"
    n = 0
    for digit in a:
        if digit!=' ':
            n*=base
            n+=digitsDic[digit]
    return n

def convert2Base(n,base,reversedigitsDic):
    "convert n in base 10 to base base using the reversedigitsDic"
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

#tests
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