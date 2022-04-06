import sys
import heapq
input = sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
  x=int(input())
  if x==0:
    if arr:
      print(-1*heapq.heappop(arr))
    else:
      print(0)
  else:
    heapq.heappush(arr,-1*x)
    
    
    
