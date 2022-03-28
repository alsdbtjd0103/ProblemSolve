import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().rstrip().split()))
a.sort()
count=0
start=1
end=n
while start<=end:
    mid=(start+end)//2
    
