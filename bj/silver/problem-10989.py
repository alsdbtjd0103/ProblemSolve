import sys
input=sys.stdin.readline
arr=[0 for _ in range(10001)]
n=int(input().rstrip())
for i in range(n):
    temp=int(input().rstrip())
    arr[temp]+=1
    
for i in range(len(arr)):
    if arr[i]!=0:
        for j in range(arr[i]):
            print(i)