MAX=1000000
n=int(input())
m=int(input())
nowch=100
arr=[]
if m!=0:
    arr=list(map(int,input().split()))
key=[0,1,2,3,4,5,6,7,8,9]
number=[]
for i in key:
    if i not in arr:
        number.append(i)
result1=MAX
result2=MAX
result3=0



if n<=nowch:
    result3=100-n
    for i in range(n,-1,-1):
        temp=list(map(int,str(i)))
        s=True
        for j in temp:
            if j not in number:
                s=False
        if s==True:
            result1=i
            break
            
    for i in range(n,nowch):
        temp=list(map(int,str(i)))
        s=True
        for j in temp:
            if j not in number:
                s=False
        if s==True:
            result2=i

            break
    result1=len(str(result1))+abs(n-result1)
    result2=len(str(result2))+abs(result2-n)
    result=min(result1,result2,result3)
else:    
    result3=n-100
    for i in range(n,100,-1):
        temp=list(map(int,str(i)))
        s=True
        for j in temp:
            if j not in number:
                s=False

        if s==True:
            result1=i
            break
            
    for i in range(n+1,MAX+1):
        temp=list(map(int,str(i)))
        s=True
        for j in temp:
            if j not in number:
                s=False
        if s==True:
            result2=i
            break
    result1=len(str(result1))+abs(n-result1)
    result2=len(str(result2))+abs(result2-n)
    result=min(result1,result2,result3)
    
# print('result1: ',result1)
# print('result2: ',result2)
# print('result3: ',result3)
    
print(result)



    
    

    
    

    
    