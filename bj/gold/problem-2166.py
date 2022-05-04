import sys
input = sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().rstrip().split())
    arr.append((x,y))

temp1,temp2 = 0,0
for i in range(0,n-1):
    temp1+=arr[i][0]*arr[i+1][1]
temp1+=arr[n-1][0]*arr[0][1]

for i in range(0,n-1):
    temp2+=arr[i+1][0]*arr[i][1]
temp2+=arr[0][0]*arr[n-1][1]

print(round(abs(temp1-temp2)/2,1))