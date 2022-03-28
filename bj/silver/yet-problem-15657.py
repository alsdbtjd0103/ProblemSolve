from itertools import combinations
import sys
input=sys.stdin.readline
n,m=map(int,input().rstrip().split())
num=[]
num=list(map(int,input().rstrip().split()))

for i in range(n):
    num+=[num[i]]*(m-1)
num.sort()
c=list(set(combinations(num,m)))
c.sort()
for i in c:
    for j in range(len(i)):
        if j==len(i)-1:
            print(i[j])
        else:
            print(i[j], end=' ')
        