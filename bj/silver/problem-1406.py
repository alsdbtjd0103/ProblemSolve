import sys
input= sys.stdin.readline

s1=input().rstrip()
s2=[]
s1=list(s1)
m=int(input())
for i in range(m):
    z=input().rstrip()
    if z[0]=='P':
        a,b=z.split()
        s1.append(b)
    elif z=='L':
        if s1:
            s2.append(s1.pop())
    elif z=='D':
        if s2:
            s1.append(s2.pop())
    elif z=='B':
        if s1: s1.pop()

s=s1+s2[::-1]
print(''.join(s))
