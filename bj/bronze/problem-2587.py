l=[]
for i in range(5):
    l.append(int(input()))
print(sum(l)//len(l))
print(sorted(l)[2])