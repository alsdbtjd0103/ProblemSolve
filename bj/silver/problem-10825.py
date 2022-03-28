n=int(input())
s=[]
for i in range(n):
    a,b,c,d=input().split()
    s.append((a,int(b),int(c),int(d)))

s.sort(key=lambda x:(-x[1],x[2],-x[3],x[0]))

for i in s:
    print(i[0])
