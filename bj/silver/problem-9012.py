t=int(input())
result=[]
for _ in range(t):
    stack=[]
    flag=True
    arr=list(input())
    if arr[0]==')' or arr[-1]=='(':
        result.append('NO')
        continue
    for v in arr:
        if v=='(':
            stack.append(v)
        else:
            if stack:
                stack.pop()
            else:
                flag=False
                break

    if not stack and flag:
        result.append('YES')
    else:
        result.append('NO')
    

for i in result:
    print(i)

