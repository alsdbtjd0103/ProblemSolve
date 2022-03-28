import sys
input=sys.stdin.readline
n=int(input().rstrip())
a=[]
for i in range(n):
    a.append(int(input().rstrip()))
    
a.sort()
for i in a:
    print(i)