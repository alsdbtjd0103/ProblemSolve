import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
s=input().rstrip()
p='I'
p+='OI'*n
cnt=0

i=0
while True:
    if i>len(s)-len(p):
        break
    if s[i]=='O':
        i+=1
    elif s[i:i+2*n+1]==p:
        cnt+=1
        i+=1
    else:
        i+=1
print(cnt)
