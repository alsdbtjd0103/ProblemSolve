n,m,k=map(int,input().split())
board=[]
for i in range(n):
    temp=list(input().split())
    z=[]
    for t in temp:
        if t=='B':
            z.append(-1)
        else: z.append(1)
        