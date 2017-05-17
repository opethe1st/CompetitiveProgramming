
fDic ={}
fDic[1]=1
fDic[2]=2
fDic[3]=4
fDic[4]=8
def f(n):
    if n in fDic:
        return fDic[n]
    else:
        fDic[n]= f(n-1)+f(n-2)+f(n-3)+f(n-4)
        return fDic[n]

print f(50)