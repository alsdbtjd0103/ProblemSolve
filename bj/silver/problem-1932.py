n=int(input())
tri=[[0]]
for i in range(n):
    tri.append(list(map(int,input().split())))


for i in range(2,n+1):
    for j in range(len(tri[i])):
        if j==0:
            tri[i][j]=tri[i-1][j]+tri[i][j]
        elif j==len(tri[i])-1:
            tri[i][j]=tri[i-1][j-1]+tri[i][j]
        else:
            tri[i][j]=max(tri[i-1][j-1],tri[i-1][j])+tri[i][j]
print(max(tri[n]))
            
        
# 어려웠던이유: dp 테이블을 무조건 만능으로 만들려고 했었기 때문인 것 같다.
# 나는 d[n]: n층까지의 최대값으로 하려고 했는데 이렇게는 불가능하다.
# 기존에 사용하던 tri 리스트를 이용하여 마치 bfs에서 최단거리를 계산할 때
# visited 리스트를 이용하듯이 tri[i][j]에 그 노드까지의 최대값을 저장한다.
# 양 끝에 있는 노드들은 그냥 바로 위의 노드까지의 최대값이랑 더하면되고
# 중간에 있는 노드들은 max(바로 위까지의 최댓값, 오른쪽 바로 위까지의 최댓값)에다가 노드값을 더하면 된다.
