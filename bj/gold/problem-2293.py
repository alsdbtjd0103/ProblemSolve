import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin=[int(input()) for i in range(n)]
dp=[0 for _ in range(k+1)]
dp[0]=1


for i in range(len(coin)):
    for j in range(coin[i],k+1):
        if j-coin[i]>=0:
            dp[j]+=dp[j-coin[i]]
print(dp[k])