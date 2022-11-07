
def hanoi(num,start,middle,dest):
    global cnt
    cnt+=1
    if num==1:
        ans.append((start,dest))
        return
    hanoi(num-1,start,dest,middle)
    hanoi(num-1,middle,start,dest)
    ans.append((start,dest))
n=int(input())
ans=[]
global cnt
cnt=0
hanoi(n,1,2,3)
print(cnt)
for x,y in ans: print(x,y)