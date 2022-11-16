import sys
input=sys.stdin.readline
n=int(input())
dist=[0 for i in range(n-1)]
dis_temp = list(map(int,input().split()))
for d in range(0,len(dis_temp)):
    dist[d]=dis_temp[d]
city=list(map(int,input().split()))

cost = city[0]
liter=0
for i in range(len(dist)):
    cost=min(cost,city[i])
    liter+=cost*dist[i]
print(liter)
