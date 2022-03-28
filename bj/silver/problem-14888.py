# 백트래킹 문제
# 1. depth 인자를 통해 종료 조건 설정
# 2. value인자와 operation 인자를 통해 탐색
# 3. if else문이 아닌 if문 만을 이용함으로써 모든 조건 탐색

n=int(input())
a=list(map(int,input().split()))
oper=list(map(int,input().split()))
maximum=-1e9
minimum=1e9
def find(depth,value,add,minus,time,divide):
    global maximum,minimum
    if depth==n-1:
        maximum=max(maximum,value)
        minimum=min(minimum,value)
        return
    if add>0:
        find(depth+1,value+a[depth+1],add-1,minus,time,divide)
    if minus>0:
        find(depth+1,value-a[depth+1],add,minus-1,time,divide)
    if time>0:
        find(depth+1,value*a[depth+1],add,minus,time-1,divide)
    if divide>0:
        if value<0:
            temp=((-1*value)//a[depth+1])*(-1)
        else:
            temp=value//a[depth+1]
        find(depth+1,temp,add,minus,time,divide-1)
        
find(0,a[0],oper[0],oper[1],oper[2],oper[3])

print(maximum)
print(minimum)
    