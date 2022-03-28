# 풀이 상상도못했다 진짜..어렵네 좀\ 더 유연한 사고가 필요할 것 같다.
import sys
import heapq
input=sys.stdin.readline
n=int(input().rstrip())
arr=[]
for i in range(n):
    heapq.heappush(arr,int(input()))
    
result=0
while len(arr)>1: 
    add=heapq.heappop(arr)+heapq.heappop(arr)
    heapq.heappush(arr,add)
    result+=add
    
print(result)
    
    
    