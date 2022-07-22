import sys
input=sys.stdin.readline

n=int(input())
p=[]
for i in range(n):
    age,name=input().rstrip().split()
    age=int(age)
    p.append((age,i,name))
p.sort()
for a,b,c in p:
    print(a,c)
