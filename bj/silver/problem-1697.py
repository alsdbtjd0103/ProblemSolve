from collections import deque

def bfs(visited,start):
    que=deque([start])
    while que:
        x=que.popleft()
        if x==k:    ## 1. 시간 줄이기 2. 0 0 일 때 0+0 은 0이라서 실행됨 -> 1이나오게됨 따라서 그걸 방지하기위해
            break
        dx.append(x)
        for i in range(3):
            nx=x+dx[i]
            if 0<=nx<maxnum and visited[nx]==0:
                visited[nx]=visited[x]+1
                que.append(nx)
        dx.pop()
maxnum=100001
dx=[-1,1]
visited=[0]*maxnum
n,k=map(int,input().split())
bfs(visited,n)
print(visited[k])