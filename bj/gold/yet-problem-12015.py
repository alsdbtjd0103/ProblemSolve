import sys
input=sys.stdin.readline
from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))

result=[]

for i in range(n):
    if not result:
        result.append(a[i])
    else:
        if a[i]>result[-1]:
            result.append(a[i])
        else:
            index=bisect_left(result,a[i])
            result[index]=a[i]
    
print(len(result))









