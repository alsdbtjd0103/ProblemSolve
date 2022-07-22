from collections import deque
n,k=map(int,input().split())
q=deque([i for i in range(1,n+1)])
result='<'
for i in range(n):
    for j in range(k-1):
        q.append(q.popleft())
    a=q.popleft()
    result+=str(a)
    if i==n-1:
        result+='>'
        continue
    result+=', '
print(result)
