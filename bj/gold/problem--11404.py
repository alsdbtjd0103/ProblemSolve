## 분명히 풀었었는데 다시풀었을 때도 똑같은 부분에서 틀림
## 입력받을때 무조건 넣는게 아니라 들어온 거리가 기존 거리보다 작아야 넣어야함

import sys
input=sys.stdin.readline
INF=1e9
n=int(input().rstrip())
m=int(input().rstrip())
distance=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,m+1):
    a,b,c=map(int,input().rstrip().split())
    distance[a][b]=min(distance[a][b],c)

for i in range(1,(n+1)):
    distance[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j]==INF:
            distance[i][j]=0
        if j==n:
            print(distance[i][j])
        else:
            print(distance[i][j],end=' ')
            