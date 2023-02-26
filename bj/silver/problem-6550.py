#97~122
s=input()
n=int(input())
words=[]
for i in range(n):
    words.append(input())

for i in range(0,26):
    flag=False
    temp=''
    for j in s:
        add = (ord(j)+i)
        if add>122:
            add=chr((add)-26)
        else:
            add=chr(add)
        temp+=add
    for w in words:
        if w in temp:
            flag=True
            break
    if flag:
        print(temp)

