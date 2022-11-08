from collections import defaultdict
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=[input().rstrip() for i in range(n)]
b=defaultdict(int)

for i in range(m):
  temp=input().rstrip()
  b[temp]+=1

add_num=0
for i in b:
  if i in a:
    add_num+=b[i]

print(add_num)