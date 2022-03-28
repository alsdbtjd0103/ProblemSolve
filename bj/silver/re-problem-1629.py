# 분할정복 문제인데 할 줄 몰라서 인터넷 검색..ㅠ
a,b,c=map(int,input().split())
def asd(a,b):
    if b==1:
        return a%c
    
    temp=asd(a,b//2)
    if b%2==0:
        return temp*temp%c
    else:
        return temp*temp*a%c
print(asd(a,b))