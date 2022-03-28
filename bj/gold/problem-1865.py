## 대표적인 벨만포드 알고리즘 11657 문제를 먼저 푼다.

tc=int(input())
for _ in range(tc):
    n,m,w=map(int,input().split())
    time=0
    worm=[[]*(n+1) for i in range(n+1)]
    path=[[]*(n+1) for i in range(n+1)]
    for i in range(m):
        s,e,t=map(int,input().split())    ##여기서 t는 걸리는 시간
        path[s][e].append(t)
        path[e][s].append(t)
    for i in range(w):
        s,e,t=map(int,input().split())  ##여기서 t는 줄어드는 시간
        worm[s][e].append(t)
    
        