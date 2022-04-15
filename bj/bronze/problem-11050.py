import sys
input=sys.stdin.readline

n,k=map(int,input().rstrip().split())
a,b=1,1
for i in range(k):
    a=a*(n-i)
for j in range(k):
    b=b*(k-j)
    
print(a//b)
