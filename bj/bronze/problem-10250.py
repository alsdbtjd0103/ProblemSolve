t=int(input())

while t>0:
    t-=1
    h,w,n=map(int,input().split())
    hotel = [[0]*(w+1) for i in range(h+1)]
    p=0
    x,y=0,0
    for i in range(1,w+1):
        for j in range(h,0,-1):
            if p==n:
                continue
            if hotel[j][i]==0:
                hotel[j][i]=1
                p+=1
                x,y=h-j+1,i
    x,y=str(x),str(y)
    if len(y)==1:
        y='0'+y
    print(x+y)

    









    # 선호도
    # 1. 엘리베이터로부터 가까운 거리 (단 ,엘리베이터는 신경쓰지 않음)
    # 2. 걷는 거리가 같을 경우 아래층 방 선호
    # 3. n번째로 도착하는 손님 방 안내
    # -> 즉 아래부터 쭉 채워가면서 한 줄 채우면 다시 아래부터 채워가는 형태