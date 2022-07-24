import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
a = []

times = []
for i in range(n):
    a.append(list(map(int, input().split())))


min_time, max_height = 1e9, -1

for height in range(0, 257):
    time = 0
    temp = b
    for i in a:
        for j in i:
            if j > height:
                temp += (j-height)
                time += (j-height)*2
            else:
                temp -= (height-j)
                time += (height-j)
    if temp >= 0:
        if time <= min_time:
            min_time = time
            max_height = height


print(min_time, max_height)
