import sys
input=sys.stdin.readline
n=int(input().rstrip())
arr=set(list(map(int,input().split())))
arr=list(arr)
arr.sort()
for i in arr:
    print(i,end=' ')
