n=int(input())
a=set()
for i in range(n):
    a.add(input())
a=list(a)
a.sort(key=lambda x:(len(x),x))

for i in a:
    print(i)