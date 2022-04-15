# 페르마의 소정리를 이용해야함.
# 그러나 마지막 출력부분은 살짝 이해는 되지만 완벽히 이해하지 못함


import sys
input=sys.stdin.readline
NUM=1000000007
n,k=map(int,input().rstrip().split())

def factorial(start):
    result=1
    for i in range(2,start+1):
        result=result*i%NUM
    return result
        
 
def square(n,k):
    if k==0: return 1
    elif k==1: return n
    temp=square(n,k//2)
    if k%2: return temp*temp*n%NUM
    else: return temp*temp%NUM
    
a=factorial(n)
b=factorial(n-k)*factorial(k)%NUM
print(a*square(b,NUM-2)%NUM)

