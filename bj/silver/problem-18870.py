import sys
from collections import defaultdict

input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=sorted(list(set(a)))
d=defaultdict(int)
for i in range(len(b)):
    d[b[i]]=i

for i in range(len(a)):
    print(d[a[i]],end=' ')
