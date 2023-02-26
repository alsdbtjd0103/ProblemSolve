from collections import deque

n=int(input())
x,y=map(int,input().split())
m=int(input())
arr=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

que = deque([])
que.append(x)
visited = [-1 for i in range(n+1)]
visited[x]=0
while que:
    q = que.popleft()
    for i in arr[q]:
        if visited[i]==-1:
            que.append(i)
            visited[i]=visited[q]+1
print(visited[y])

