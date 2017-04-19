#!/bin/python

import sys
def isVowel(letter):
    vowels = set(list('aeiouy')) 
    if letter in vowels:
        return True
    else:
        return False

def isBeautiful(word):
    for i in xrange(1,len(word)):
        if (isVowel(word[i-1]) and isVowel(word[i]) )or word[i-1]==word[i]:
            return False
    else:
        return True

w = raw_input().strip()
# Print 'Yes' if the word is beautiful or 'No' if it is not.
if isBeautiful(w):
    print 'Yes'
else:
    print 'No'
