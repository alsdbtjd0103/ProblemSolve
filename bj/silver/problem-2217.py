import sys
input=sys.stdin.readline

n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

a.sort()

ans=0
for i in range(n):
    ans=max(ans,a[i]*(n-i))
print(ans)
