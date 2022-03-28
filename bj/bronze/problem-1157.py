arr=input().upper()
arr2=set(arr)
maxnum=0
result=''
for i in arr2:
    temp=arr.count(i)
    if temp>maxnum:
        maxnum=temp
        result=i
        

for i in arr2:
    if i==result:
        continue
    if arr.count(i)==maxnum:
        result='?'
        
print(result)
    
            
        
            
            
