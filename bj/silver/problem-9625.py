k=int(input())

ans=[(1,0)]
for i in range(k):
    a,b=ans[-1]
    na,nb = b,a+b
    ans.append((na,nb))

print(ans[-1][0],ans[-1][1])