t=int(input())
ans=[]
for _ in range(t):
    result=0
    score=0
    arr=list(input())
    for i in arr:
        if i=='O':
            score+=1
            result+=score
        elif i=='X':
            score=0
    ans.append(result)
for i in ans:
    print(i)
            
    