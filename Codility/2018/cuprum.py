import string


LOWERCASE_LETTERS_AND_DIGITS_DICT = {letter: index for index, letter in enumerate(string.ascii_lowercase + string.digits)}


def solution(S):
    # signatures keeps track of the letters that occur an odd number of times in string, S[:index+1]
    signatures = [0]+[0]*len(S)
    for index, letter in enumerate(S):
        signatures[index+1] = signatures[index]^(1<<LOWERCASE_LETTERS_AND_DIGITS_DICT[letter])

    longestValidStringLength = 0
    # signatureExtremaDict keeps track of the max and min positions where this signature is found - between these positions a number occurs
    # an even number of times
    signatureExtremaDict = {}
    for index, signature in enumerate(signatures):
        if signature in signatureExtremaDict:
            signatureExtremaDict[signature] = (signatureExtremaDict[signature][0], index)
        else:
            signatureExtremaDict[signature] = (index, index)
    # longestValidStringLength is the maxlength of a substring with all characters appearing an even number of times
    for signature, extrema in signatureExtremaDict.items():
        longestValidStringLength = max(longestValidStringLength, max(extrema)-min(extrema))
    return longestValidStringLength

# Simple test
print(solution(S='bbaba'))
