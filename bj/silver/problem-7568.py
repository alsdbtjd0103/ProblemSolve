n=int(input())
person=[]
for _ in range(n):
    x,y=map(int,input().split())
    person.append((x,y))

result=[1 for i in range(n)]
for p in range(len(person)):
    px,py=person[p]
    for i in person:
        ix,iy=i
        if px<ix and py<iy:
            result[p]+=1
for r in result:
    print(r)
            

