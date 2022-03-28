n,k=map(int,input().split())
item=[]
for i in range(n):
    w,v=map(int,input().split())
    item.append((w,v))

d=[[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if item[i-1][0]>j:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j],d[i-1][j-item[i-1][0]]+item[i-1][1])

print(d[n][k])

# 0/1 배낭문제로 좀 더 이해해야할 것 같다.
# 우선 여기서 d[n][k] 는 n개의 물품 중에서 k의 무게만큼 되도록 선택하여 가치가 최대가 되는 값을 가지고 있다.
# 따라서 item을 순서대로 쭉 검사해 나가면서
# if item의 무게>j 이면 가방에 못넣기 때문에 d[i][j]=d[i-1][j]와 같고
# else d[i][j]=d[i-1][j] or d[i-1][j-아이템무게]+item가치 둘 중 큰 것을 선택

    