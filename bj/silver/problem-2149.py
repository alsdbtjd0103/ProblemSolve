key=input()
s=input()

key2=[]
for i in range(len(key)):
    key2.append((key[i],i))

key2.sort()

term = len(s)//len(key)
result=[[] for i in range(len(key))]
for i in range(len(s)):
    result[i//term].append(s[i])

result2=[[] for i in range(len(key))]

for i in range(len(key2)):
    a,b=key2[i]
    result2[b]=result[i]



answer=''
for i in range(term):
    for j in range(len(result2)):
        answer+=result2[j][i]
print(answer)

