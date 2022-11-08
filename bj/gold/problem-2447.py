n=int(input())

def recur(num):
    if num==1:
        return ['*']
    stars = recur(num//3)
    ans=[]
    for s in stars:
        ans.append(s*3)
    for s in stars:
        ans.append(s+' '*(num//3)+s)
    for s in stars:
        ans.append(s*3)
    return ans


result=recur(n)
for i in result:
    print(i)