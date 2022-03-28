def gen_d(a):
    remain=0

    for i in str(a):
        remain+=int(i)
    return a+remain

data=[0]*10001
for i in range(10001):
    temp=gen_d(i)
    if temp>10000:
        continue
    data[temp]=1
for k in range(len(data)):
    if data[k]==0:
        print(k)