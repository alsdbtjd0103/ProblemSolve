t=int(input())
data=[]
for i in range(t):
    data.append(int(input()))
d=[0]*11
d[1]=1
d[2]=2
d[3]=4
for x in range(4,11):
    d[x]=d[x-1]+d[x-2]+d[x-3]
    
for y in data:
     print(d[y])
    

#dp 문제로 규칙을 찾는게 조건
#규칙은 d[x]=d[x-1]+d[x-2]+d[x-3]
#이유:
#    d[x]:
#        1하나 더 추가 후, d[x-1]
#        2하나 더 추가 후, d[x-2]
#        3하나 더 추가 후, d[x-3]

    
        