s=input()
result=[]
for i in range(0,len(s)):
    for j in range(0,len(s)):
        result.append(s[j:j+i+1])

result=list(set(result))

print(len(result))