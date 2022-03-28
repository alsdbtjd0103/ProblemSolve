##e드디어 5트만에 어느정도 알고리즘을 이해했다.
# 이진탐색을 할 때 무조건 노드를 찾기위해 탐색하는 것이 아니라 문제에서
# 무엇을 요구하는지 확인해야할 것 같다.
# 이 문제에서는 최대 거리를 요구하고 있다. 따라서 start end mid 모두
# 최대 거리(gap)를 대입해서풀어야한다.
# 이 알고리즘은 최대거리를 찾는 알고리즘으로 앞에서부터 하나씩 gap이상인 노드에 count+=1을 통해 공유기를 설치하고 c보다 더 많거나 c만큼 설치가 가능하다면 gap을 늘려서 다시 처음부터 설치하면서 탐색하는 알고리즘이다.

import sys
input=sys.stdin.readline
n,c=map(int,input().rstrip().split())
house=[]
for i in range(n):
    house.append(int(input().rstrip()))
house.sort()
start=1
end=house[-1]-house[0]
result=0
while start<=end:
    temp=house[0]
    gap=(end+start)//2
    count=1
    for i in range(1,n):
        if house[i]>=temp+gap:
            count+=1
            temp=house[i]
    if count>=c:
        start=gap+1
        result=max(result,gap)
    else:
        end=gap-1
print(result)
        
        