# bisect 사용법을 착각하고 있어서 계속 막혔었다.
# bisect left를 했을 때,  a=[1,2,3,5,8] 이고 bisect_left(a,4) 를 하면 0을 반환하는게 아니라 
# 3을 반환한다. 3과 5 사이이기 때문이다. 

import sys
from bisect import bisect_left
input=sys.stdin.readline
n=int(input().rstrip())
a=list(map(int,input().rstrip().split()))
m=int(input().rstrip())
b=list(map(int,input().rstrip().split()))

a.sort()


for i in b:
    temp=bisect_left(a,i)
    if temp==n:
        print(0)
        continue
    if a[temp]==i:
        print(1)
    else:
        print(0)