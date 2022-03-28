#알고리즘은 동작하나 kmp알고리즘을 사용하지 않아서 시간초과..ㅠㅠ

import sys
input=sys.stdin.readline
t=input().rstrip()
p=input().rstrip()

start=p[0]
end=p[-1]
length=len(p)
count=0
result=[]
s=-1
e=1

while True:
    s=t.find(start,s+1)
    
    if s==-1 or e==-1:
        break
    while True:  
        if (e-s)==length-1:
            if p==t[s:e+1]:
                count+=1
                result.append(s)
                break
            else:
                break
        elif (e-s)<length:
            e=t.find(end,e+1)
            if e==-1:
                break
        else:
            break
print(count)
for i in result:
    print(i+1)
                