from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
q=deque([])
for i in range(n):
    o=input().rstrip()
    if o[:2]=='pu':
        a,b=o.split()
        q.append(int(b))
    elif o=='pop':
        if q:   print(q.popleft())
        else:   print(-1)
    elif o=='size':
        print(len(q))
    elif o=='empty':
        if q:   print(0)
        else:   print(1)
    elif o=='front':
        if q:   
            temp=q.popleft()
            print(temp)
            q.appendleft(temp)
        else:   print(-1)
    elif o=='back':
        if q:
            print(q[-1])
        else:   print(-1)
