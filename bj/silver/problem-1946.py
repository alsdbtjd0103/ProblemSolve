import sys
input=sys.stdin.readline

t=int(input())
result=[]
for _ in range(t):
    n=int(input())
    score=[]
    for i in range(n):
        a,b=map(int,input().split())
        score.append((a,b))

    score.sort()
    ans=1
    temp=score[0][1]
    for x,y in score:
        if y<temp:
            ans+=1
            temp=y
    result.append(ans)
    

for r in result:
    print(r)
