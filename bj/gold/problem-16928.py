from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[i for i in range(101)]

for _ in range(n):
    x,y=map(int,input().split())
    a[x]=y

for _ in range(m):
    x,y=map(int,input().split())
    a[x]=y

q=deque([1])
dice=[1,2,3,4,5,6]
visited=[-1 for _ in range(101)]
visited[1]=0

while q:
    x=q.popleft()
    if x==100:
        break
    for d in dice:
        nx = x+d
        if 1<=nx<=100 and visited[nx]==-1:
            visited[nx]=visited[x]+1
            q.append(a[nx])
            if visited[a[nx]]==-1:
                visited[a[nx]]=visited[nx]


            

print(visited[100])


