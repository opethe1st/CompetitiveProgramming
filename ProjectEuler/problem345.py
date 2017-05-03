
def bestMatrixSum(startRow,setOfCols):
    #print startRow,setOfCols
    def hamming_weight(x):
		return bin(x).count("1")
    if startRow == ROWS:
			#assert hamming_weight(setOfCols) == COLUMNS - ROWS
			return 0
    if maxSum[startRow][setOfCols]==0:
        maxi = 0
        col=0
        while (1<<col)<=setOfCols:
            if setOfCols & (1<<col) != 0:
                maxi = max(maxi,Ar[startRow][col] +bestMatrixSum(startRow+1,setOfCols^(1<<col)))
            col+=1
        maxSum[startRow][setOfCols]=maxi
    return maxSum[startRow][setOfCols]

Ar = []
for _ in xrange(15):
    Ar.append(map(int,raw_input().split()))
#print Ar
ROWS = len(Ar)
COLUMNS = len(Ar[0])
maxSum= [[0 for i in xrange(1<<15)] for j in xrange(15)]
print bestMatrixSum(0,(1<<15)-1)