import time
start = time.time()
def isPalindrome(num):
    return str(num) == str(num)[::-1]
squares = [i*i for i in xrange(2,100000)]
cubes =  [i**3 for i in xrange(20,1000)]
squarecube = {}
for square in squares:
    for cube in cubes:
        num = square+cube
        if isPalindrome(num):
            squarecube[num]=squarecube.get(num,0)+1
for val in squarecube:
    if squarecube[val]==4:
        print val
print time.time()-start