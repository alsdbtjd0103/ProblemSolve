## sys로 안하면 시간초과
## sys로하고 python3로 하면 통과

import sys
input=sys.stdin.readline
n=int(input().rstrip())
arr=[]
for i in range(n):
    x,y=map(int,input().rstrip().split())
    arr.append((x,y))
    
arr.sort()
for x,y in arr:
    print(x,y)
    
    
    
 ## problem-11651 
import sys
input=sys.stdin.readline
n=int(input().rstrip())
arr=[]
for i in range(n):
    x,y=map(int,input().rstrip().split())
    arr.append((x,y))
    
arr.sort(key=lambda x:(x[1],x[0]))
for x,y in arr:
    print(x,y)