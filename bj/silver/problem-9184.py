from collections import defaultdict

basic =0
dic=defaultdict(lambda:basic)

def w(a,b,c):
    if dic[(a,b,c)]!=basic:
        return dic[(a,b,c)]

    if a<=0 or b<=0 or c<=0:
        dic[(a,b,c)]=1
        return 1

    if a>20 or b>20 or c>20:
        if dic[(a,b,c)]==basic:
            dic[(a,b,c)]=w(20,20,20)
        return dic[(a,b,c)]

    if a<b and b<c:
        dic[(a,b,c)]=w(a, b, c-1)+w(a, b-1, c-1)-w(a,b-1,c)
        return dic[(a,b,c)]

    dic[(a,b,c)]=w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)
    return dic[(a,b,c)]


while True:
    a,b,c=map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print('w(%d, %d, %d) = %d'%(a,b,c,w(a,b,c)))
    

