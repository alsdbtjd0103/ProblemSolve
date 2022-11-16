import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
q=deque([])
for _ in range(n):
    a=list(map(str,input().rstrip().split()))
    if a[0]=='push': q.append(a[1])
    elif a[0]=='pop':
        if q: print(q.popleft())
        else: print(-1)
    elif a[0]=='front':
        if q: print(q[0])
        else: print(-1)
    elif a[0]=='size':  print(len(q))
    elif a[0]=='empty': 
        if q:   print(0)
        else:   print(1)
    elif a[0]=='back':
        if q:   print(q[-1])
        else:   print(-1)

    