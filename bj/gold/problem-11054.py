import sys
n=int(input())
a=[0]
temp=list(map(int,input().rstrip().split()))
for i in temp:
    a.append(i)

dp_ac = [1 for i in range(n+1)]
dp_dec = [[0]*(n+1)]

for i in range(1,n+1):
    for j in range(1,i):
        if a[i]>a[j]:
            dp_ac[i]=max(dp_ac[i],dp_ac[j]+1)
  
        
for i in range(1,n+1):
    t_list = a[i:]
    t_dp = [1 for z in range(len(t_list))]
    for j in range(0,len(t_list)):
        for k in range(0,j):
            if t_list[j]<t_list[k]:
                t_dp[j]=max(t_dp[j],t_dp[k]+1)
    dp_dec.append([0]*i+t_dp)


ans=-1
for i in range(1,n+1):
    ans=max(ans,dp_ac[i]+max(dp_dec[i])-1)
print(ans)
                

