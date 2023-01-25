n=int(input())
tp = []
dp=[0]*(n+1)
for _ in range(n):
    tp.append(map(int,input().split()))

for i in range(n-1,-1,-1):
    t,p=tp[i]
    if t+i>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],dp[i+t]+p)

print(max(dp))




    
    
    
        