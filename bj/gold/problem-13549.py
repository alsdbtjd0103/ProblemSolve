from collections import deque
Max=100001
def bfs(visited,start):
    que=deque([start])
    while que:
        
        x=que.popleft()
        if x==k:
            break
        dx=[x,-1,1]
        nxx=[]
        for i in range(3):
            nx=x+dx[i]
            if 0<=nx<Max and visited[nx]==0 and nx not in nxx:
                if i!=0:
                    que.append(nx)
                    visited[nx]=visited[x]+1
                else:
                    que.append(nx)
                    visited[nx]=visited[x]
                nxx.append(nx)
            
                
                    
                
    
    
n,k=map(int,input().split())
visited=[0]*Max
bfs(visited,n)
print(visited[k])

