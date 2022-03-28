# 처음엔 permutation을 이용해서 할라고 했는데 max가 십만이라서 
# 순열 조합들이 너무 많아 메모리초과가 된다.
# 그래서 검색을 통해 해결..
# 다시풀어보장
from collections import deque

def bfs(visited,start):
    que=deque([start])
    visited[start][0]=0 ##시작 위치(방문처리)
    visited[start][1]=1 ##거친 횟수
    
    while que:

        x=que.popleft()
        dx.append(x)
        for i in range(3):
            nx=x+dx[i]
            if 0<=nx<maxnum:
                if visited[nx][0]==-1: ##한번도 방문 안했으면
                    visited[nx][0]=visited[x][0]+1
                    visited[nx][1]=visited[x][1] ##한번도 방문 안했으니까 +1하면되지않나 근데 이러면 1 8 넣으면 1나옴 (2나와야함)
                    #이거 이유가 1때문이다. 1*2=2 1+1=2 라서 맨처음에 1이 pop될때 2가 하나만 들어가게됨. 따라서 
                    que.append(nx)
            
                elif visited[nx][0]==visited[x][0]+1:
                    visited[nx][1]+=visited[x][1] ##중복된 좌표이기 때문에 기존에 방문했던 값에다가 새로 더함

        dx.pop()
        
maxnum=100001
dx=[-1,1]
visited=[[-1,0] for _ in range(maxnum)] 

n,k=map(int,input().split())
bfs(visited,n)
time=visited[k][0]
count=visited[k][1]
print(time)
print(count)