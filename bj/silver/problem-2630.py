from string import whitespace
import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().rstrip().split())))
global white
global blue
white, blue = 0, 0


def divAndCon(x, y, N):
    global white, blue
    color = a[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != a[i][j]:
                divAndCon(x, y, N//2)
                divAndCon(x, y+N//2, N//2)
                divAndCon(x+N//2, y, N//2)
                divAndCon(x+N//2, y+N//2, N//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


divAndCon(0, 0, n)
print(white)
print(blue)
