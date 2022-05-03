import sys
input = sys.stdin.readline

n=int(input())
dp=[[0,0] for i in range(n+1)]
result=[n]
dp[1][1]=1
for i in range(2,n+1):
    temp=[] # temp안에 최소의 dp값과 dp인덱스 저장
    dp[i][0]=dp[i-1][0]+1
    temp.append((dp[i][0]-1,i-1)) # 여기서 1 빼거나 아래에서 append할 때 1더해야함
    if i%2==0:
        temp.append((dp[i//2][0],i//2))
        dp[i][0]=min(dp[i][0],dp[i//2][0]+1)
    if i%3==0:
        temp.append((dp[i//3][0],i//3))
        dp[i][0]=min(dp[i][0],dp[i//3][0]+1)
    temp.sort()
    dp[i][1] = temp[0][1]
    
print(dp[n][0])

temp=n
while True:
    value,index = dp[temp]
    result.append(index)
    temp=index
    if temp==1:
        break
if n==1: # 1일때 1 1 형식으로 나와서 틀림
    print(1)
else:
    for i in result:
        print(i,end=' ')


