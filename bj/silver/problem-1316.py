def group_word(word):
    temp=''
    for k in range(len(word)-1):
        if word[k]!=word[k+1]:
            temp+=word[k]
                
    temp+=word[-1]
    
    for i in range(len(temp)-1):
        for k in range(i,len(temp)-1):
            if temp[i]==temp[k+1]:
                return False
    return True 

n=int(input())
temp=[]
for _ in range(n):
    temp.append(input())
count=0
          
for i in temp:
    result=group_word(i)
    if result:
        count+=1

print(count)
    
                