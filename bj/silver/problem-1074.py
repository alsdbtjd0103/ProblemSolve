n,r,c = map(int,input().split())

answer = 0
size = 2**n

while True:
    if r<size//2:
        if c<size//2:
            pass
        else:
            answer+=(size*size)//4
            c=c-size//2
    else:
        if c<size//2:
            r=r-size//2
            answer+=(size*size)//2
        else:
            r=r-size//2
            c=c-size//2
            answer+=int((size*size*0.75))
    size=size//2
    if size==0:
        print(answer)
        break

            

