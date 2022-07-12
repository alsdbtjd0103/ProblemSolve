n,m=map(int,input().split())
office=[]
cctv=[]

for i in range(n):
    office.append(list(map(int,input().split())))
    for c in range(len(office[i])):
        if office[i][c]!=0:
            cctv.append((i,c))


def dictect(d,x,y):
    if d=='RIGHT':
        for i in range(y+1,m):
            if office[x][i]==0:
                office[x][i]='#'
            else:
                break
    elif d=='LEFT':
        for i in range(y-1,-1,-1):
            if office[x][i]==0:
                office[x][i]='#'
            else:
                break
    elif d=='UP':
        for i in range(x-1,-1,-1):
            if office[i][y]==0:
                office[i][y]='#'
            else:
                break
    elif d=='DOWN':
        for i in range(x+1,n):
            if office[i][y]==0:
                office[i][y]='#'
            else:
                break


def watch(x,y):
    num = office[x][y]
    if num==1:
        dictect('RIGHT',x,y)
    if num ==2:
        dictect('RIGHT',x,y)
        dictect('LEFT',x,y)
        
    if num==3:
        dictect('UP',x,y)
        dictect('RIGHT',x,y)
    if num==4:
        dictect('UP',x,y)
        dictect('RIGHT',x,y)
        dictect('LEFT',x,y)
    if num==5:
        dictect('LEFT',x,y)
        dictect('RIGHT',x,y)
        dictect('UP',x,y)
        dictect('DOWN',x,y)

while 
cnt=0
for i in range(n):
    for j in range(m):
        if office[i][j]==0:
            cnt+=1

for i in office:
    print(i)
print(cnt)

