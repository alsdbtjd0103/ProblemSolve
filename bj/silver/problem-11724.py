def dfs(graph,v):
    visited[v]=True
    for i in range(1,n+1):
        if graph[v][i] and visited[i]==False:
                   dfs(graph,i)
    
    
n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x][y], graph[y][x]=1,1

visited=[False]*(n+1)
count=0
for k in range(1,n+1):
    if visited[k]==False:
        dfs(graph,k)
        count+=1
        
print(count)

# dfs, bfs 뭘로 하던지 딱히 상관은 없다.
# 여기서 포인트는 visited 배열을 dfs함수 인자로 받는 것이 아니라 전역변수로
# 설정하는 것이다.
# 그렇게되면 visited 리스트는 초기화 되지 않아서 한번 dfs를 호출하면 이미 방문한
# 노드들은 false로 바뀌게되고 다음번에 dfs를 호출할 때는 그것들을 제외할 수 있게된다. 
# 그런데 여기서 단점은 python3로 실행하게되면 recursion error(재귀오류)가
# 발생하여 pypy3로 실행하여야 한다. 이걸 생각하면 bfs로 하는것도 나쁘지 않을 것 같다. 아니면 sys를 import하여 sys.setrecursionlimit(10000)으로 설정
        

   

