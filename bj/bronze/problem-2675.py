t=int(input())
result=[]
for _ in range(t):
    r,s=input().split()
    r=int(r)
    temp=''

    for i in s:
        temp+=i*r
    result.append(temp)
for i in result:
    print(i)