n=int(input())
MAX_INT = 1e9
dp=[MAX_INT]*(n+1)

for i in range(1,n+1):
    if i==2 or i==5:
        dp[i]=1
    elif i==4:
        dp[i]=2
    elif i>=5:
        dp[i]=min(dp[i],dp[i-2]+1,dp[i-5]+1)

for i in range(0,len(dp)):
    if dp[i]>=MAX_INT:
        dp[i]=-1

print(dp[n])