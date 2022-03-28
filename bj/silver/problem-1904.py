n=int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(3)
else:
    dp=[0 for _ in range(n+1)]
    dp[1],dp[2],dp[3]=1,2,3
    for i in range(4,n+1):
        dp[i]=(dp[i-2]+dp[i-1])%15746
    print(dp[n])