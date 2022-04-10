import sys
import heapq
input=sys.stdin.readline
t=int(input())
while t>0:
  t-=1
  k=int(input())
  maxH=[]
  minH=[]
  visited=[False for i in range(1000001)]
  for i in range(k):
    char,num=input().rstrip().split()
    num=int(num)
    if char=='I':
      heapq.heappush(maxH,(-num,i))
      heapq.heappush(minH,(num,i))
      visited[i]=True
    elif num==1:
      while maxH and not visited[maxH[0][1]]: heapq.heappop(maxH) #minH와 동기화
      if maxH: 
        visited[maxH[0][1]]=False
        heapq.heappop(maxH)
    else:
      while minH and not visited[minH[0][1]]: heapq.heappop(minH) #maxH와 동기화
      if minH:
        visited[minH[0][1]]=False
        heapq.heappop(minH)

  while maxH and not visited[maxH[0][1]]: heapq.heappop(maxH)
  while minH and not visited[minH[0][1]]: heapq.heappop(minH)
  if maxH:
    print(-maxH[0][0],minH[0][0])
  else:
    print("EMPTY")
    
    
      
        
        
