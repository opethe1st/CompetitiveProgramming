#!/bin/python
import time
import sys
import random
class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		self.prev = None

class LinkedList(object) :
    def __init__( self ) :
        self.head = None		

    def add( self, data ) :
        node = Node( data )
        if self.head == None :	
            self.head = node
        else :
            node.next = self.head
            node.next.prev = node						
            self.head = node			

    def remove( self, p ):
        #temp = p.prev
        current = p
        #print 'remove',p.prev.data,p.data,p.next.data
        #print 'before',
        #lprint(self)
        next = current.next
        prev = current.prev
        prev.next = next
        next.prev = prev
        #print "after",
        #lprint(self)
    
def lprint(s):
    node = s.head
    print 's',
    while node is not None:
        print node.data,
        node=node.next
    print
    
    
def solution(arr):
    #print s
    s = LinkedList()
    s.head = None
    for data in arr:
        s.add(data)
    node=s.head   
    #lprint(s)
    count = 0
    while True:
        found = False
        i=s.head
        while i.next is not None and i.next.next is not None:
            #print 'i',i.next.data
            if i.data==0 and i.next.next.data==0:
                s.remove(i.next) #USE A linked liat? constant popping
                #lprint(s)
                count+=1
                found= True
            i=i.next
        if not found:
            break
    if count%2==1:
        return True
    else:
        return False
start = time.time()
a = [random.randint(0,1) for i in xrange(1000000) ]

g = 100000#int(raw_input().strip())
for a0 in xrange(g):
    n = 10#int(raw_input().strip())
    sequence = [random.randint(0,1) for i in xrange(n) ]#map(int, raw_input().strip().split(' '))
    if solution(sequence):
        print 'Alice'
    else:
        print 'Bob'
print time.time()-start