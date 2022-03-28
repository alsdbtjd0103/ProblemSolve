# 시작하는 순서가 아니라 끝나는 순서대로 정렬하는게 포인트

import sys
import heapq
input=sys.stdin.readline

n=int(input().rstrip())
meet=[]

for i in range(n):
    a,b=map(int,input().rstrip().split())
    heapq.heappush(meet,(b,a))
last_time=0
count=0
while meet:
    end,start=heapq.heappop(meet)
    if start>=last_time:
        last_time=end
        count+=1
print(count)
