
import sys
input=sys.stdin.readline
n=int(input())
u=[]
for i in range(n):
    u.append(int(input()))
twosum=[]
answer=0
u.sort(reverse=True)
for i in range(len(u)):
    for j in range(i,len(u)):
        a=u[i]+u[j]
        if a<=u[0]:
            twosum.append(a)

for i in range(len(u)):
    flag=False
    for t in twosum:
        if (u[i]-t) in u:
             answer=max(u[i],answer)
             flag=True
             break
    if flag:
        break

print(answer)

