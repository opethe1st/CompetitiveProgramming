"""IEEE Extreme 10.0
start with all the numbers partitioned into n sets. then look for the lowest difference two consecutive numbers 
and merge those two numbers into a group. Now you have n-1 elements.. do the same thing again till you have k groups.. """
def dogGroup(d,k):
    d.sort()
    diff = [d[i+1]-d[i] for i in xrange(len(d)-1)]
    diff.sort()
    return sum(diff[:len(d)-k])

#Some tests.
d = dogGroup([2,3,6,7,11,13,17,23,29,31],8)
print d
print dogGroup([20,30,40,41,50],1)
print dogGroup([1,1,3,5],2)