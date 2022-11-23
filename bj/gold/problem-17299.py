from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = defaultdict(int)
for i in a:
    b[i] += 1
stack = []
result = []
for i in range(len(a)):
    while stack:
        index = stack[-1]
        if b[a[index]] < b[a[i]]:
            stack.pop()
            result.append((index, a[i]))
        else:
            break
    stack.append(i)

for s in stack:
    result.append((s, -1))

result.sort()
for i in result:
    print(i[1], end=' ')
