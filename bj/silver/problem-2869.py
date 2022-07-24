import math
a,b,v=map(int,input().split())

dis=a-b

temp = math.ceil(v/dis)

while True:
    temp-=1
    if a*temp-b*(temp-1)<v:
        print(temp+1)
        break