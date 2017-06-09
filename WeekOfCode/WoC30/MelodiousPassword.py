#!/bin/python
import time
import sys
start = time.time()
Vowels = 'aeiou'
Consonants = 'bcdfghjklmnpqrstvwxz'
def generateConsonant(n):
    #print "Consonant",n
    if n==1:
        return list(Consonants)
    else:
        res = []
        for k in Consonants:
            passwords = generateVowel(n-1)
            for password in passwords:
                res.append(k+password)
        return res
def generateVowel(n):
    #print "Vowel",n
    if n==1:
        return list(Vowels)
    else:
        res = []
        for v in Vowels:
            #print "here"
            passwords = generateConsonant(n-1)
            for password in passwords:
                
                res.append(v+password)
        return res

def n7():
    count = 0
    for v1 in Vowels:
        for k1 in Consonants:
            for v2 in Vowels:
                for k2 in Consonants:
                    for v3 in Vowels:
                        for k3 in Consonants:
                            for v4 in Vowels:
                                print k1#v1+k1+v2+k2+v3+k3
                                count+=1
    
    for k1 in Consonants:
        for v2 in Vowels:
            for k2 in Consonants:
                for v3 in Vowels:
                    for k3 in Consonants:
                        for v1 in Vowels:
                            for k4 in Consonants:
                                print k1#+v2+k2+v3+k3+v1+k4
                                count+=1
    return count
#n = int(raw_input().strip())
#passwords = generateVowel(n)+generateConsonant(n)
#for password in passwords:
#    print password
#    pass
n7()
print time.time()-start