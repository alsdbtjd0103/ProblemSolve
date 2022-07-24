from collections import defaultdict
t=int(input())
result=[]
for _ in range(t):
    n=int(input())
    kind=set()
    dic=defaultdict(int)
    ans=1
    for i in range(n):
        a,b=input().split()
        dic[b]+=1
        kind.add(b)
    for k in kind:
        ans*=(dic[k]+1)
    ans-=1
    result.append(ans)
for r in result:
    print(r)

