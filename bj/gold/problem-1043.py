## 대강의 풀이 방법은 먼저 진실을 아는 사람들이 방문하는 파티 표시하고
## 그 파티에 있는 사람들이 방문하는 파티들을 모두 표시한다음
## 표시가 안된, 즉 진실을 아는 사람들이 아무도 없는 파티만 세면 된다.
from collections import deque

def check():
    party_num=[]
    while true_people:
        person=true_people.popleft()
        for i in range(m):
            if person in party[i]:
                if i not in party_num:
                    party_num.append(i)
                    for p in party[i]:
                        true_people.append(p)
    return len(party_num)
            
            
                    

n,m=map(int,input().split())
temp=list(map(int,input().split()))
party=[]
num_true=temp[0]
true_people=deque([])


for i in range(1,num_true+1):
    true_people.append(temp[i])
    
for i in range(m):
    input_temp=list(map(int,input().split()))
    party.append(input_temp[1:])

true_party_num=check()
result=m-true_party_num
print(result)


