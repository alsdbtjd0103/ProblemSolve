import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=-1e9
s=0
for i in range(0,n-k+1):
    if i==0: 
        s=sum(a[:k])
    else:
        s-=a[i-1]
        s+=a[i+k-1]
    ans=max(s,ans)

print(ans)