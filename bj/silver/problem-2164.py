from collections import deque
n=int(input())
q=deque([i for i in range(1,n+1)])
result=-1
while q:
    result=q.popleft()
    if len(q)>1:
        q.append(q.popleft())
print(result)


