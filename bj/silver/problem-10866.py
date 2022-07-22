from collections import deque
import sys
input=sys.stdin.readline
q=deque([])
n=int(input())
for i in range(n):
    o=input().rstrip()
    if o[:4]=='push':
        a,b=o.split()
        if a=='push_front':
            q.appendleft(int(b))
        else:
            q.append(int(b))
    elif o=='pop_front':
        if q:   print(q.popleft())
        else:   print(-1)
    elif o=='pop_back':
        if q:   print(q.pop())
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
            temp=q.pop()
            print(temp)
            q.append(temp)
        else:   print(-1)
