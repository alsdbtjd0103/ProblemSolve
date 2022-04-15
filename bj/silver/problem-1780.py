import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().rstrip().split())) for i in range(n)]
result=[0,0,0]

def divAndCon(x,y,N):
    value=a[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if value!=a[i][j]:
                divAndCon(x,y,N//3)
                divAndCon(x,y+N//3,N//3)
                divAndCon(x,y+N//3+N//3,N//3)
                divAndCon(x+N//3,y,N//3)
                divAndCon(x+N//3+N//3,y,N//3)
                divAndCon(x+N//3,y+N//3,N//3)
                divAndCon(x+N//3,y+N//3+N//3,N//3)
                divAndCon(x+N//3+N//3,y+N//3,N//3)
                divAndCon(x+N//3+N//3,y+N//3+N//3,N//3)
                return
    result[value+1]+=1
divAndCon(0,0,n)
for i in result:
    print(i)
