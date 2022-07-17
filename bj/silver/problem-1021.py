
n, m = map(int, input().split())
loc = list(map(int, input().split()))
global q
q = []
num = 0


def left():
    temp = q.pop(0)
    q.append(temp)


def right():
    global q
    temp = q.pop()
    q = [temp]+q[:]


for i in range(1, n+1):
    q.append(i)
value = []
for l in loc:
    value.append(q[l-1])

for v in value:
    index = -1
    for i in range(len(q)):
        if q[i] == v:
            index = i
            break
    if index <= len(q)//2:
        while True:

            if q[0] == v:
                q.pop(0)
                break
            left()
            num += 1

    else:
        while True:
            if q[0] == v:
                q.pop(0)
                break
            right()
            num += 1


print(num)
