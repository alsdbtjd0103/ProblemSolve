n=int(input())
answer = ['CY','SK']
dp=[0]*(n+1)

if n<4:
    print(answer[n%2])
if n>=4:
    dp[1],dp[3]=1,1
    dp[2]=2
    for i in range(4,n+1):
        dp[i]=min(dp[i-1]+1,dp[i-3]+1)
    print(answer[dp[n]%2])

    
